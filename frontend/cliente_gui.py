import sys
import PySimpleGUI as sg
from omniORB import CORBA

# Importar o módulo gerado pelo omniidl a partir do IDL
import ParqueamentoApp


class ClienteCorbaApp:

    def __init__(self):
        # 1. Inicializar o ORB CORBA
        self.orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

        # Usar corbaloc para obter a referência do NameService
        # Altere o IP e a Porta conforme a configuração do seu Naming Service
        corbaloc = "corbaloc:iiop:127.0.0.1:1050/NameService"
        obj = self.orb.string_to_object(corbaloc)

        import CosNaming

        self.ncRef = obj._narrow(CosNaming.NamingContext)

        # 2. Resolver as referências das interfaces no NameService
        self.servico_usuario = self._obter_servico(
            "UsuarioService", ParqueamentoApp.Usuario
        )
        self.servico_parque = self._obter_servico(
            "ParqueService", ParqueamentoApp.Parque
        )
        self.servico_vaga = self._obter_servico(
            "VagaService", ParqueamentoApp.Vaga
        )
        self.servico_viatura = self._obter_servico(
            "ViaturaService", ParqueamentoApp.Viatura
        )
        self.servico_reserva = self._obter_servico(
            "ReservaService", ParqueamentoApp.Reserva
        )

        # Guarda o utilizador autenticado após o login
        self.usuario_logado = None

    def _obter_servico(self, nome_servico, interface_class):
        import CosNaming

        path = [CosNaming.NameComponent(nome_servico, "")]
        obj = self.ncRef.resolve(path)
        return obj._narrow(interface_class)

    # ==========================================
    # TELA DE LOGIN / CADASTRO
    # ==========================================
    def janela_login(self):
        sg.theme("DarkBlue3")

        layout = [
            [
                sg.Text(
                    "Sistema de Parqueamento",
                    font=("Helvetica", 16, "bold"),
                    justification="center",
                    expand_x=True,
                )
            ],
            [sg.HSeparator()],
            [
                sg.Text("Telefone:", size=(10, 1)),
                sg.Input(key="-LOGIN-TEL-", size=(25, 1)),
            ],
            [
                sg.Text("Senha:", size=(10, 1)),
                sg.Input(key="-LOGIN-SENHA-", password_char="*", size=(25, 1)),
            ],
            [
                sg.Button("Entrar", key="-BTN-LOGIN-", bind_return_key=True),
                sg.Button("Criar Conta", key="-BTN-TELA-CADASTRO-"),
            ],
            [sg.HSeparator()],
            # Painel expansível de cadastro
            [
                sg.Column(
                    [
                        [
                            sg.Text("Nome:"),
                            sg.Input(key="-CAD-NOME-", size=(25, 1)),
                        ],
                        [
                            sg.Text("Telefone:"),
                            sg.Input(key="-CAD-TEL-", size=(25, 1)),
                        ],
                        [
                            sg.Text("Senha:"),
                            sg.Input(
                                key="-CAD-SENHA-",
                                password_char="*",
                                size=(25, 1),
                            ),
                        ],
                        [
                            sg.Button(
                                "Registar Utilizador", key="-BTN-CADAGRAR-"
                            )
                        ],
                    ],
                    key="-PAINEL-CADASTRO-",
                    visible=False,
                )
            ],
        ]

        return sg.Window(
            "Autenticação - Cliente CORBA",
            layout,
            element_justification="c",
            finalize=True,
        )

    # ==========================================
    # TELA PRINCIPAL (DASHBOARD)
    # ==========================================
    def janela_principal(self):
        sg.theme("DarkBlue3")

        # Aba 1: Parques e Vagas
        tab_parques = [
            [
                sg.Text("Pesquisar Parques por Categoria (Província/Nome):"),
                sg.Input(key="-PESQUISA-CAT-", size=(20, 1)),
                sg.Button("Pesquisar", key="-BTN-PESQUISAR-PARQUES-"),
            ],
            [
                sg.Table(
                    values=[],
                    headings=[
                        "ID",
                        "Nome",
                        "Província",
                        "Localização",
                        "Telefone",
                        "Preço/h",
                        "Cobertura",
                    ],
                    auto_size_columns=False,
                    col_widths=[5, 15, 12, 15, 12, 10, 10],
                    display_row_numbers=False,
                    justification="center",
                    key="-TABELA-PARQUES-",
                    enable_events=True,
                    select_mode=sg.TABLE_SELECT_MODE_SINGLE,
                    expand_x=True,
                    expand_y=True,
                )
            ],
            [
                sg.Text("Vagas Disponíveis no Parque Selecionado:"),
                sg.Combo(
                    [],
                    key="-COMBO-VAGAS-",
                    size=(30, 1),
                    readonly=True,
                    expand_x=True,
                ),
                sg.Button("Atualizar Vagas", key="-BTN-CARREGAR-VAGAS-"),
            ],
        ]

        # Aba 2: Minhas Viaturas
        tab_viaturas = [
            [
                sg.Table(
                    values=[],
                    headings=["ID", "Marca", "Modelo", "Matrícula"],
                    auto_size_columns=False,
                    col_widths=[8, 15, 15, 15],
                    key="-TABELA-VIATURAS-",
                    expand_x=True,
                    expand_y=True,
                )
            ],
            [
                sg.Button("Atualizar Lista", key="-BTN-LISTAR-VIATURAS-"),
                sg.Button("Remover Selecionada", key="-BTN-REMOVER-VIATURA-"),
            ],
            [sg.HSeparator()],
            [
                sg.Text(
                    "Adicionar Nova Viatura", font=("Helvetica", 11, "bold")
                )
            ],
            [
                sg.Text("Marca:", size=(8, 1)),
                sg.Input(key="-ADD-MARCA-", size=(15, 1)),
                sg.Text("Modelo:", size=(8, 1)),
                sg.Input(key="-ADD-MODELO-", size=(15, 1)),
            ],
            [
                sg.Text("Matrícula:", size=(8, 1)),
                sg.Input(key="-ADD-MATRICULA-", size=(15, 1)),
                sg.Button("Adicionar Viatura", key="-BTN-ADD-VIATURA-"),
            ],
        ]

        # Aba 3: Reservas
        tab_reservas = [
            [
                sg.Text("Fazer Nova Reserva", font=("Helvetica", 11, "bold")),
            ],
            [
                sg.Text("ID Vaga:"),
                sg.Input(key="-RES-VAGA-ID-", size=(10, 1)),
                sg.Text("ID Viatura:"),
                sg.Input(key="-RES-VIATURA-ID-", size=(10, 1)),
            ],
            [
                sg.Text("Data Entrada (YYYY-MM-DD):"),
                sg.Input(key="-RES-DATA-E-", size=(12, 1)),
                sg.Text("Hora (HH:MM:SS):"),
                sg.Input(key="-RES-HORA-E-", size=(10, 1)),
            ],
            [
                sg.Text("Data Saída (YYYY-MM-DD):    "),
                sg.Input(key="-RES-DATA-S-", size=(12, 1)),
                sg.Text("Hora (HH:MM:SS):"),
                sg.Input(key="-RES-HORA-S-", size=(10, 1)),
            ],
            [
                sg.Text("Preço Estimado Total:"),
                sg.Input(key="-RES-PRECO-", size=(10, 1), default_text="0.0"),
                sg.Button("Confirmar Reserva", key="-BTN-CRIAR-RESERVA-"),
            ],
            [sg.HSeparator()],
            [sg.Text("Minhas Reservas Ativas", font=("Helvetica", 11, "bold"))],
            [
                sg.Table(
                    values=[],
                    headings=[
                        "ID",
                        "Vaga",
                        "Viatura",
                        "Entrada",
                        "Hora E.",
                        "Saída",
                        "Hora S.",
                        "Total",
                    ],
                    auto_size_columns=False,
                    col_widths=[5, 6, 8, 12, 10, 12, 10, 8],
                    key="-TABELA-RESERVAS-",
                    expand_x=True,
                    expand_y=True,
                )
            ],
            [sg.Button("Listar Minhas Reservas", key="-BTN-LISTAR-RESERVAS-")],
        ]

        # Aba 4: Perfil / Conta
        tab_perfil = [
            [
                sg.Text(
                    "Atualizar Meus Dados", font=("Helvetica", 11, "bold")
                )
            ],
            [
                sg.Text("Nome:", size=(10, 1)),
                sg.Input(
                    key="-PERFIL-NOME-",
                    default_text=self.usuario_logado.nome,
                    size=(25, 1),
                ),
            ],
            [
                sg.Text("Telefone:", size=(10, 1)),
                sg.Input(
                    key="-PERFIL-TEL-",
                    default_text=self.usuario_logado.telefone,
                    size=(25, 1),
                ),
            ],
            [
                sg.Text("Nova Senha:", size=(10, 1)),
                sg.Input(
                    key="-PERFIL-SENHA-",
                    default_text=self.usuario_logado.senha,
                    password_char="*",
                    size=(25, 1),
                ),
            ],
            [
                sg.Button(
                    "Salvar Alterações", key="-BTN-ATUALIZAR-PERFIL-"
                )
            ],
        ]

        layout_main = [
            [
                sg.Text(
                    f"Bem-vindo(a), {self.usuario_logado.nome}!",
                    font=("Helvetica", 12, "bold"),
                ),
                sg.Push(),
                sg.Button("Sair/Logout", key="-BTN-LOGOUT-", button_color="red"),
            ],
            [
                sg.TabGroup(
                    [
                        [
                            sg.Tab("Parques & Vagas", tab_parques),
                            sg.Tab("Minhas Viaturas", tab_viaturas),
                            sg.Tab("Reservas", tab_reservas),
                            sg.Tab("Meu Perfil", tab_perfil),
                        ]
                    ],
                    expand_x=True,
                    expand_y=True,
                )
            ],
        ]

        return sg.Window(
            "Sistema de Parqueamento - Cliente CORBA",
            layout_main,
            size=(800, 550),
            resizable=True,
            finalize=True,
        )

    # ==========================================
    # LOOP PRINCIPAL DA APLICAÇÃO
    # ==========================================
    def executar(self):
        win_login = self.janela_login()
        win_main = None

        while True:
            # Captura de eventos da janela ativa
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                window.close()
                if window == win_main:
                    win_main = None
                elif window == win_login:
                    break
                if win_login is None and win_main is None:
                    break

            # ----------------------------------------------------
            # EVENTOS: TELA DE LOGIN / CADASTRO
            # ----------------------------------------------------
            if window == win_login:
                if event == "-BTN-TELA-CADASTRO-":
                    # Alternar visibilidade do painel de cadastro
                    visivel = win_login["-PAINEL-CADASTRO-"].visible
                    win_login["-PAINEL-CADASTRO-"].update(visible=not visivel)

                elif event == "-BTN-LOGIN-":
                    tel = values["-LOGIN-TEL-"].strip()
                    senha = values["-LOGIN-SENHA-"].strip()

                    try:
                        # Chamada CORBA ao serviço de autenticação
                        user_dto = self.servico_usuario.login(tel, senha)

                        if user_dto and user_dto.id_usuario > 0:
                            self.usuario_logado = user_dto
                            sg.popup("Login efetuado com sucesso!", title="Sucesso")
                            win_login.close()
                            win_login = None
                            win_main = self.janela_principal()
                        else:
                            sg.popup_error("Telefone ou senha incorretos.")
                    except Exception as e:
                        sg.popup_error(f"Erro de comunicação CORBA: {e}")

                elif event == "-BTN-CADAGRAR-":
                    nome = values["-CAD-NOME-"].strip()
                    tel = values["-CAD-TEL-"].strip()
                    senha = values["-CAD-SENHA-"].strip()

                    if nome and tel and senha:
                        # Tipo 2 = Cliente normal
                        novo_user = ParqueamentoApp.UsuarioDTO(
                            -1, nome, tel, senha, 2
                        )
                        try:
                            self.servico_usuario.cadastrar(novo_user)
                            sg.popup(
                                "Cadastro efetuado! Já pode realizar o login."
                            )
                            win_login["-PAINEL-CADASTRO-"].update(visible=False)
                        except Exception as e:
                            sg.popup_error(f"Erro ao cadastrar: {e}")
                    else:
                        sg.popup_warning("Preencha todos os campos do cadastro.")

            # ----------------------------------------------------
            # EVENTOS: TELA PRINCIPAL (DASHBOARD)
            # ----------------------------------------------------
            elif window == win_main:

                if event == "-BTN-LOGOUT-":
                    self.usuario_logado = None
                    win_main.close()
                    win_main = None
                    win_login = self.janela_login()

                # --- PARQUES ---
                elif event == "-BTN-PESQUISAR-PARQUES-":
                    categoria = values["-PESQUISA-CAT-"].strip()
                    try:
                        parques = self.servico_parque.pesquisarPorCategoria(
                            categoria
                        )
                        dados_tabela = [
                            [
                                p.id_parque,
                                p.nome,
                                p.provincia,
                                p.localizacao,
                                p.telefone,
                                f"{p.preco:.2f}",
                                p.cobertura,
                            ]
                            for p in parques
                        ]
                        win_main["-TABELA-PARQUES-"].update(values=dados_tabela)
                    except Exception as e:
                        sg.popup_error(f"Erro ao pesquisar parques: {e}")

                elif event == "-BTN-CARREGAR-VAGAS-":
                    selecionados = values["-TABELA-PARQUES-"]
                    if selecionados:
                        linha_idx = selecionados[0]
                        # Pega o ID do Parque na primeira coluna da tabela
                        id_parque = int(
                            win_main["-TABELA-PARQUES-"].get()[linha_idx][0]
                        )
                        try:
                            vagas = (
                                self.servico_vaga.listarVagasDisponiveis(
                                    id_parque
                                )
                            )
                            lista_vagas_str = [
                                f"ID Vaga: {v.id_vaga} - Num: {v.numero_vaga}"
                                for v in vagas
                            ]
                            win_main["-COMBO-VAGAS-"].update(
                                values=lista_vagas_str
                            )
                        except Exception as e:
                            sg.popup_error(f"Erro ao carregar vagas: {e}")
                    else:
                        sg.popup_warning(
                            "Selecione primeiro um parque na tabela acima."
                        )

                # --- VIATURAS ---
                elif event == "-BTN-LISTAR-VIATURAS-":
                    try:
                        viaturas = self.servico_viatura.listarViaturas(
                            self.usuario_logado.id_usuario
                        )
                        dados_v = [
                            [v.id_viatura, v.marca, v.modelo, v.matricula]
                            for v in viaturas
                        ]
                        win_main["-TABELA-VIATURAS-"].update(values=dados_v)
                    except Exception as e:
                        sg.popup_error(f"Erro ao listar viaturas: {e}")

                elif event == "-BTN-ADD-VIATURA-":
                    marca = values["-ADD-MARCA-"].strip()
                    modelo = values["-ADD-MODELO-"].strip()
                    matricula = values["-ADD-MATRICULA-"].strip()

                    if marca and modelo and matricula:
                        nova_v = ParqueamentoApp.ViaturaDTO(
                            -1,
                            marca,
                            modelo,
                            matricula,
                            self.usuario_logado.id_usuario,
                        )
                        try:
                            self.servico_viatura.adicionarViatura(nova_v)
                            sg.popup("Viatura adicionada com sucesso!")
                            # Limpar campos
                            win_main["-ADD-MARCA-"].update("")
                            win_main["-ADD-MODELO-"].update("")
                            win_main["-ADD-MATRICULA-"].update("")
                        except Exception as e:
                            sg.popup_error(f"Erro ao adicionar viatura: {e}")

                elif event == "-BTN-REMOVER-VIATURA-":
                    sel = values["-TABELA-VIATURAS-"]
                    if sel:
                        id_v = int(
                            win_main["-TABELA-VIATURAS-"].get()[sel[0]][0]
                        )
                        try:
                            self.servico_viatura.removerViatura(id_v)
                            sg.popup("Viatura removida!")
                        except Exception as e:
                            sg.popup_error(f"Erro ao remover viatura: {e}")

                # --- RESERVAS ---
                elif event == "-BTN-CRIAR-RESERVA-":
                    try:
                        id_vaga = int(values["-RES-VAGA-ID-"])
                        id_viatura = int(values["-RES-VIATURA-ID-"])
                        data_e = values["-RES-DATA-E-"]
                        hora_e = values["-RES-HORA-E-"]
                        data_s = values["-RES-DATA-S-"]
                        hora_s = values["-RES-HORA-S-"]
                        preco = float(values["-RES-PRECO-"])

                        reserva = ParqueamentoApp.ReservaDTO(
                            -1,
                            data_e,
                            hora_e,
                            data_s,
                            hora_s,
                            preco,
                            id_vaga,
                            self.usuario_logado.id_usuario,
                            id_viatura,
                        )

                        self.servico_reserva.criarReserva(reserva)
                        sg.popup("Reserva criada com sucesso!")
                    except ValueError:
                        sg.popup_warning(
                            "Verifique se os IDs e o preço são números válidos."
                        )
                    except Exception as e:
                        sg.popup_error(f"Erro ao criar reserva: {e}")

                elif event == "-BTN-LISTAR-RESERVAS-":
                    try:
                        reservas = self.servico_reserva.listarReservas(
                            self.usuario_logado.id_usuario
                        )
                        dados_r = [
                            [
                                r.id_reserva,
                                r.id_vaga,
                                r.id_viatura,
                                r.data_entrada,
                                r.hora_entrada,
                                r.data_saida,
                                r.hora_saida,
                                f"{r.preco_total:.2f}",
                            ]
                            for r in reservas
                        ]
                        win_main["-TABELA-RESERVAS-"].update(values=dados_r)
                    except Exception as e:
                        sg.popup_error(f"Erro ao listar reservas: {e}")

                # --- PERFIL ---
                elif event == "-BTN-ATUALIZAR-PERFIL-":
                    nome = values["-PERFIL-NOME-"].strip()
                    tel = values["-PERFIL-TEL-"].strip()
                    senha = values["-PERFIL-SENHA-"].strip()

                    u_updated = ParqueamentoApp.UsuarioDTO(
                        self.usuario_logado.id_usuario,
                        nome,
                        tel,
                        senha,
                        self.usuario_logado.tipo,
                    )

                    try:
                        sucesso = self.servico_usuario.actualizarDados(
                            u_updated
                        )
                        if sucesso:
                            self.usuario_logado = u_updated
                            sg.popup("Perfil atualizado com sucesso!")
                        else:
                            sg.popup_error("Não foi possível atualizar o perfil.")
                    except Exception as e:
                        sg.popup_error(f"Erro ao atualizar perfil: {e}")


if __name__ == "__main__":
    app = ClienteCorbaApp()
    app.executar()