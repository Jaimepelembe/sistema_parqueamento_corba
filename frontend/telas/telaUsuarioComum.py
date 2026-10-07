import PySimpleGUI as sg
from marcasModelosCarro import dicionarioMarcasModelos

# Define o tema do PySimpleGUI
sg.theme('DarkBlue3')


class TelaUsuarioComum:
    def __init__(self,usuario_logado,listaParques, listaViaturas,listaTransacoes,listaReservas,saldoActual):
        self.usuario_logado= usuario_logado
        self.saldo_atual = saldoActual  # Exemplo de saldo inicial em Meticais (MT)
        self.lista_parques =listaParques
        self.minhas_viaturas = listaViaturas
        self.minhas_transacoes = listaTransacoes
        self.minhas_reservas = listaReservas
        self.dicionarioCarros=dicionarioMarcasModelos
        
        self.iniciar_janela_principal()



    # --- MONTAGEM DAS TABS PRINCIPAIS ---

    def _criar_tab_parques(self):
        headings = ['Nome', 'Província', 'Localização', 'Telefone', 'Horário', 'Cobertura', 'Preço (MT)']
        return [
            [sg.Text('Parques de Estacionamento Disponíveis', font=('Helvetica', 12, 'bold'))],
            [
                sg.Table(
                    values=self.lista_parques,
                    headings=headings,
                    auto_size_columns=True,
                    justification="left",
                    num_rows=16,
                    key='-TABELA_PARQUES-',
                    enable_events=True,
                    select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                )
            ],
            [sg.Text('Clique em uma linha da tabela para realizar a reserva da vaga.', font=('Helvetica', 9, 'italic'))],
        ]

    def _criar_tab_viaturas(self):
        return [
            [sg.Text('Adicionar Nova Viatura', font=('Helvetica', 12, 'bold'))],
            [
                sg.Text('Marca:'),
                sg.Combo(list(self.dicionarioCarros.keys()), key="-MARCA-", enable_events=True ,readonly=True, size=(25, 1)),
                sg.Text('Modelo:'),
                sg.Combo([], key="-MODELO-", enable_events=False,  readonly=True, size=(25, 1)),
                sg.Text('Matrícula:'),
                sg.Input(default_text="Ex: ABC 126 MP",key='-MATRICULA-', size=(15, 1)),
            ],
            [sg.Button('Cadastrar Viatura', key='-BTN_ADD_VIATURA-')],
            [sg.HSeparator()],
            [sg.Text('Minhas Viaturas Cadastradas', font=('Helvetica', 12, 'bold'))],
            [
                sg.Table(
                    values=self.minhas_viaturas,
                    headings=['Marca', 'Modelo', 'Matrícula'],
                    auto_size_columns=True,
                    justification="center",
                    num_rows=6,
                    key='-TABELA_VIATURAS-',
                )
            ],
        ]

    def _criar_tab_perfil(self):
        return [
            [sg.Text('Atualizar Meus Dados', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome:    '), sg.Input(default_text=self.usuario_logado.nome, key='-PERFIL_NOME-', size=(30, 1))],
            [sg.Text('Telefone:'), sg.Input(default_text=self.usuario_logado.telefone, key='-PERFIL_TEL-', size=(30, 1))],
            [sg.Text('Senha:   '), sg.Input(default_text=self.usuario_logado.senha, password_char='*', key='-PERFIL_SENHA-', size=(30, 1))],
            [sg.Button('Atualizar Dados', key='-BTN_ATUALIZAR_PERFIL-')],
            [sg.HSeparator()],
            [sg.Text('Informações da Conta & Depósito', font=('Helvetica', 12, 'bold'))],
            [sg.Text(f'Saldo Atual: {self.saldo_atual:.2f} MT', font=('Helvetica', 11, 'bold'), key='-TXT_SALDO-')],
            [
                sg.Text('Valor a Depositar (MT):'),
                sg.Input(key='-VALOR_DEPOSITO-', size=(15, 1)),
                sg.Button('Depositar', key='-BTN_DEPOSITAR-'),
            ],
            [sg.Text('Histórico de Transações', font=('Helvetica', 10, 'bold'))],
            [
                sg.Table(
                    values=self.minhas_transacoes,
                    headings=['ID','Tipo', 'Valor','Estado','Data', 'Hora'],
                    col_widths=[5, 10, 10, 12,12,10],
                    justification="center",
                    auto_size_columns=False,
                    num_rows=6,
                    key='-TABELA_TRANSACOES-',
                )
            ],
        ]

    def _criar_tab_reservas(self):
        return [

            [sg.Text('Histórico de reservas', font=('Helvetica', 12, 'bold'))],
            [
                sg.Table(
                    values=self.minhas_reservas,
                    headings=['ID','Data Entrada', 'Hora Entrada','Data Saida','Hora Saida', 'Preco','ID Vaga','Matricula Viatura'],
                    col_widths=[5, 12, 12, 12,12,10,10,15],
                    justification="center",
                    auto_size_columns=False,
                    num_rows=10,
                    key='-TABELA_RESERVAS-',
                )
            ],
        ]




    def iniciar_janela_principal(self):
        layout = [
            [
                sg.TabGroup([
                    [
                        sg.Tab('Parques', self._criar_tab_parques()),
                        sg.Tab('Minhas Viaturas', self._criar_tab_viaturas()),
                        sg.Tab('Meu Perfil', self._criar_tab_perfil()),
                        sg.Tab("Minhas Reservas",self._criar_tab_reservas())
                    ]
                ])
            ],
            [sg.Button('Sair do Sistema', key='-SAIR-')],
        ]
        self.window = sg.Window('Sistema de Gestão de Parqueamento', layout, finalize=True)


    def fechar(self):
        self.window.close()

    def ocultar(self):
        self.window.hide()

    def exibir(self):
        self.window.un_hide()


    # --- JANELA SECUNDÁRIA: RESERVA DE VAGA ---


    # --- CONTROLADOR PRINCIPAL DE EVENTOS ---

"""
    def executar(self):
        self.iniciar_janela_principal()

        while True:
            window, event, values = sg.read_all_windows()

            # Fechar aplicação
            if window == self.window_principal and event in (sg.WIN_CLOSED, '-SAIR-'):
                break

            # 1. EVENTOS DA TAB PARQUES (Seleção na Tabela para Reserva)
            if window == self.window_principal and event == '-TABELA_PARQUES-':
                linhas_selecionadas = values['-TABELA_PARQUES-']
                if linhas_selecionadas:
                    indice = linhas_selecionadas[0]
                    parque_selecionado = self.lista_parques[indice]
                    nome_parque = parque_selecionado[0]
                    preco_parque = parque_selecionado[6]

                    if not self.minhas_viaturas:
                        sg.popup_error('Erro', 'Você precisa cadastrar pelo menos uma viatura antes de reservar.')
                    else:
                        self.window_principal.hide()
                        self.window_reserva = self.abrir_janela_reserva(nome_parque, preco_parque)

            # 2. EVENTOS DA TELA DE RESERVA
            if self.window_reserva and window == self.window_reserva:
                if event in (sg.WIN_CLOSED, '-CANCELAR_RESERVA-'):
                    self.window_reserva.close()
                    self.window_reserva = None
                    self.window_principal.un_hide()

                elif event == '-BTN_CONFIRMAR_RESERVA-':
                    vaga = values['-RESERVA_VAGA-']
                    matricula = values['-RESERVA_MATRICULA-']
                    data_e = values['-RESERVA_DATA-']
                    hora_e = values['-RESERVA_HORA-']
                    minuto_e = values['-RESERVA_MINUTO-']

                    msg = (
                        f'Reserva Confirmada com Sucesso!\n\n'
                        f'• Vaga: {vaga}\n'
                        f'• Viatura: {matricula}\n'
                        f'• Data/Hora Entrada: {data_e} às {hora_e}:{minuto_e}'
                    )
                    sg.popup('Confirmação', msg)

                    self.window_reserva.close()
                    self.window_reserva = None
                    self.window_principal.un_hide()

            # 3. EVENTOS DA TAB MINHAS VIATURAS
            if window == self.window_principal and event == '-BTN_ADD_VIATURA-':
                marca = values['-MARCA-'].strip()
                modelo = values['-MODELO-'].strip()
                matricula = values['-MATRICULA-'].strip()

                if marca and modelo and matricula:
                    nova_viatura = [marca, modelo, matricula]
                    self.minhas_viaturas.append(nova_viatura)

                    # Atualiza a tabela na tela
                    self.window_principal['-TABELA_VIATURAS-'].update(values=self.minhas_viaturas)

                    # Limpa os campos de entrada
                    self.window_principal['-MARCA-'].update('')
                    self.window_principal['-MODELO-'].update('')
                    self.window_principal['-MATRICULA-'].update('')

                    sg.popup('Sucesso', f'Viatura {matricula} cadastrada com sucesso!')
                else:
                    sg.popup_error('Erro de Validação', 'Por favor, preencha todos os campos da viatura.')

            # 4. EVENTOS DA TAB MEU PERFIL
            if window == self.window_principal and event == '-BTN_ATUALIZAR_PERFIL-':
                nome = values['-PERFIL_NOME-'].strip()
                tel = values['-PERFIL_TEL-'].strip()
                senha = values['-PERFIL_SENHA-'].strip()

                if nome and tel and senha:
                    self.usuario_logado = nome
                    sg.popup('Sucesso', 'Seus dados foram atualizados com sucesso!')
                else:
                    sg.popup_error('Erro de Validação', 'Nenhum campo do perfil pode ficar vazio.')

            if window == self.window_principal and event == '-BTN_DEPOSITAR-':
                valor_str = values['-VALOR_DEPOSITO-'].strip()
                try:
                    valor = float(valor_str)
                    if valor > 0:
                        self.saldo_atual += valor
                        data_hoje = datetime.now().strftime('%d/%m/%Y')

                        # Atualiza transações e saldo
                        self.minhas_transacoes.append([data_hoje, 'Depósito em Conta', f'+{valor:.2f} MT'])
                        self.window_principal['-TXT_SALDO-'].update(f'Saldo Atual: {self.saldo_atual:.2f} MT')
                        self.window_principal['-TABELA_TRANSACOES-'].update(values=self.minhas_transacoes)
                        self.window_principal['-VALOR_DEPOSITO-'].update('')

                        sg.popup('Sucesso', f'Depósito de {valor:.2f} MT realizado com sucesso!')
                    else:
                        sg.popup_error('Erro', 'Informe um valor maior que zero.')
                except ValueError:
                    sg.popup_error('Erro', 'Informe um número válido para o depósito.')

        self.window_principal.close()


if __name__ == '__main__':
    app = TelaUsuarioComum()
    app.executar()
    
    """