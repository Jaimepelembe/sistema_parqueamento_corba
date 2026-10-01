import PySimpleGUI as sg

class TelaPrincipal:

  def __init__(self,usuario_logado):
        sg.theme("DarkBlue3")
        
    

        # Aba 1: Parques e Vagas
        tab_parques = [
            [
                sg.Text("Pesquisar Parques por Categoria (Província,Nome ou Preço):"),
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
                    select_mode=sg.TABLE_CLICKED_INDICATOR,  #TABLE_SELECT_MODE_SINGLE
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
                    default_text= nome, #self.usuario_logado.
                    size=(25, 1),
                ),
            ],
            [
                sg.Text("Telefone:", size=(10, 1)),
                sg.Input(
                    key="-PERFIL-TEL-",
                    default_text=telefone, #self.usuario_logado.
                    size=(25, 1),
                ),
            ],
            [
                sg.Text("Nova Senha:", size=(10, 1)),
                sg.Input(
                    key="-PERFIL-SENHA-",
                    default_text=senha #self.usuario_logado.
                    ,
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
                    f"Bem-vindo(a), {nome}!", #self.usuario_logado.
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

        self.window= sg.Window(            "Sistema de Parqueamento - Cliente CORBA",
            layout_main,
            #size=(800, 550),
            resizable=True,
           #finalize=True,
        )


