from datetime import datetime
import PySimpleGUI as sg

# Define o tema do PySimpleGUI
sg.theme('DarkBlue3')


class SistemaParqueamento:
    def __init__(self, usuario_logado: str):
        self.usuario_logado = usuario_logado
        self.saldo_atual = 500.00  # Exemplo de saldo inicial em Meticais (MT)

        # Listas de dados para popular a interface (Simulação de Banco de Dados)
        self.lista_parques = [
            ['Parque Central', 'Maputo', 'Av. 24 de Julho', '841234567', '07:00 - 22:00', 'COBERTO', 50.0],
            ['Parque Baixa', 'Maputo', 'Rua da Bagamoyo', '829876543', '24 Horas', 'NAO_COBERTO', 30.0],
            ['Parque Matola', 'Maputo', 'Av. das Indústrias', '865554433', '08:00 - 20:00', 'COBERTO', 40.0],
        ]

        self.minhas_viaturas = [
            ['Toyota', 'Ractis', 'ABC-123-MC'],
            ['Nissan', 'Hardbody', 'AAB-456-MP'],
        ]

        self.minhas_transacoes = [
            ['30/09/2026', 'Depósito', '+500.00 MT'],
            ['29/09/2026', 'Reserva Parque Central', '-50.00 MT'],
        ]

        # Janelas
        self.window_principal = None
        self.window_reserva = None

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
                    num_rows=8,
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
                sg.Input(key='-MARCA-', size=(15, 1)),
                sg.Text('Modelo:'),
                sg.Input(key='-MODELO-', size=(15, 1)),
                sg.Text('Matrícula:'),
                sg.Input(key='-MATRICULA-', size=(15, 1)),
            ],
            [sg.Button('Cadastrar Viatura', key='-BTN_ADD_VIATURA-')],
            [sg.HSeparator()],
            [sg.Text('Minhas Viaturas Cadastradas', font=('Helvetica', 12, 'bold'))],
            [
                sg.Table(
                    values=self.minhas_viaturas,
                    headings=['Marca', 'Modelo', 'Matrícula'],
                    auto_size_columns=True,
                    num_rows=6,
                    key='-TABELA_VIATURAS-',
                )
            ],
        ]

    def _criar_tab_perfil(self):
        return [
            [sg.Text('Atualizar Meus Dados', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome:    '), sg.Input(default_text=self.usuario_logado, key='-PERFIL_NOME-', size=(30, 1))],
            [sg.Text('Telefone:'), sg.Input(default_text='841234567', key='-PERFIL_TEL-', size=(30, 1))],
            [sg.Text('Senha:   '), sg.Input(default_text='123456', password_char='*', key='-PERFIL_SENHA-', size=(30, 1))],
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
                    headings=['Data', 'Descrição', 'Valor'],
                    auto_size_columns=True,
                    num_rows=5,
                    key='-TABELA_TRANSACOES-',
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
                    ]
                ])
            ],
            [sg.Button('Sair do Sistema', key='-SAIR-')],
        ]
        self.window_principal = sg.Window('Sistema de Gestão de Parqueamento', layout, finalize=True)

    # --- JANELA SECUNDÁRIA: RESERVA DE VAGA ---

    def abrir_janela_reserva(self, nome_parque: str, preco_parque: float):
        # Gerar opções de horas (00 a 23) e minutos (00, 15, 30, 45)
        horas = [f'{h:02d}' for h in range(24)]
        minutos = ['00', '15', '30', '45']

        # Extrai matrículas para a caixa de seleção
        matriculas_disponiveis = [v[2] for v in self.minhas_viaturas]
        vagas_disponiveis = ['Vaga A-01', 'Vaga A-02', 'Vaga B-05', 'Vaga B-06', 'Vaga C-10']

        # Data de hoje padrão
        hoje = datetime.now()

        layout_reserva = [
            [sg.Text(f'Reservar Vaga - {nome_parque}', font=('Helvetica', 13, 'bold'))],
            [sg.Text(f'Preço por Hora: {preco_parque:.2f} MT')],
            [
                sg.Text('Selecionar Vaga:    '),
                sg.Combo(
                    vagas_disponiveis,
                    default_value=vagas_disponiveis[0] if vagas_disponiveis else '',
                    key='-RESERVA_VAGA-',
                    readonly=True,
                    size=(20, 1),
                ),
            ],
            [
                sg.Text('Selecionar Viatura:'),
                sg.Combo(
                    matriculas_disponiveis,
                    default_value=matriculas_disponiveis[0] if matriculas_disponiveis else '',
                    key='-RESERVA_MATRICULA-',
                    readonly=True,
                    size=(20, 1),
                ),
            ],
            [
                sg.Text('Data de Entrada:    '),
                sg.Input(
                    default_text=hoje.strftime('%Y-%m-%d'),
                    key='-RESERVA_DATA-',
                    size=(12, 1),
                    readonly=True,
                ),
                sg.CalendarButton(
                    'Escolher Data',
                    target='-RESERVA_DATA-',
                    format='%Y-%m-%d',
                    default_date_m_d_y=(hoje.month, hoje.day, hoje.year),
                ),
            ],
            [
                sg.Text('Hora de Entrada:    '),
                sg.Combo(horas, default_value='08', key='-RESERVA_HORA-', readonly=True, size=(5, 1)),
                sg.Text(':'),
                sg.Combo(minutos, default_value='00', key='-RESERVA_MINUTO-', readonly=True, size=(5, 1)),
                sg.Text('hrs'),
            ],
            [sg.Button('Confirmar Reserva', key='-BTN_CONFIRMAR_RESERVA-'), sg.Button('Cancelar', key='-CANCELAR_RESERVA-')],
        ]

        return sg.Window('Efetuar Reserva', layout_reserva, modal=True, finalize=True)

    # --- CONTROLADOR PRINCIPAL DE EVENTOS ---

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
    app = SistemaParqueamento('João Silva')
    app.executar()