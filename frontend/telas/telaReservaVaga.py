from datetime import datetime
import PySimpleGUI as sg


class TelaReservaVaga:
    
    def __init__(self, minhas_viaturas, parqueSelecioinado,vagasDisponiveis):
        
        self.minhas_viaturas=minhas_viaturas
        self.parque_selecionado=parqueSelecioinado
        self.vagas_disponiveis=vagasDisponiveis

        # Gerar opções de horas (00 a 23) e minutos (00, 15, 30, 45)
        horas = [f'{h:02d}' for h in range(24)]
        minutos = ['00', '15', '30', '45']

        # Extrai matrículas para a caixa de seleção
        matriculas_disponiveis = [v[2] for v in self.minhas_viaturas]
        #self.vagas_disponiveis = ['Vaga A-01', 'Vaga A-02', 'Vaga B-05', 'Vaga B-06', 'Vaga C-10']

        # Data de hoje padrão
        hoje = datetime.now()

        layout_reserva = [
            [sg.Text(f'Reservar Vaga - {self.parque_selecionado.nome}', font=('Helvetica', 13, 'bold'))],
            [sg.Text(f'Preço por Hora: {self.parque_selecionado.preco:.2f} MT')],
            [
                sg.Text('Selecionar Vaga:    '),
                sg.Combo(
                    self.vagas_disponiveis,
                    default_value=self.vagas_disponiveis[0] if self.vagas_disponiveis else '',
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
            
                  # Campo para Data de Entrada
       [
           sg.Text('Data de Entrada:', size=(15, 1)),
           sg.Input(key='-DT-ENTRADA-', size=(15, 1), readonly=True),
           sg.CalendarButton(
               'Escolher Data',
               target='-DT-ENTRADA-',
               format='%Y-%m-%d',
               button_color=('white', '#1f77b4'),
               title='Selecione a Data de entrada'
           )
       ],
                  
             # Campo para Hora de Entrada
            [
                sg.Text('Hora de entrada:    '),
                sg.Combo(horas, default_value='08', key='-RESERVA-HORA-ENTRADA-', readonly=True, size=(5, 1)),
                sg.Text(':'),
                sg.Combo(minutos, default_value='00', key='-RESERVA-MINUTO-ENTRADA-', readonly=True, size=(5, 1)),
                sg.Text('hrs'),
            ],
            
        
      # Campo para Data de Saída
       [
           sg.Text('Data de Saída:', size=(15, 1)),
           sg.Input(key='-DT-SAIDA-', size=(15, 1), readonly=True),
           sg.CalendarButton(
               'Escolher Data',
               target='-DT-SAIDA-',
               format='%Y-%m-%d',
               button_color=('white', '#1f77b4'),
               title='Selecione a Data de Saída'
           )
       ],
            
            
             # Campo para Hora de Saída
            [
                sg.Text('Hora de Saída:    '),
                sg.Combo(horas, default_value='08', key='-RESERVA-HORA-SAIDA-', readonly=True, size=(5, 1)),
                sg.Text(':'),
                sg.Combo(minutos, default_value='00', key='-RESERVA-MINUTO-SAIDA-', readonly=True, size=(5, 1)),
                sg.Text('hrs'),
            ],
            [sg.Button('Confirmar Reserva', key='-BTN_CONFIRMAR_RESERVA-'), sg.Button('Cancelar', key='-CANCELAR_RESERVA-')],
        ]

        self.window= sg.Window('Efetuar Reserva', layout_reserva, modal=True, finalize=True)


    def fechar(self):
        self.window.close()

    def ocultar(self):
        self.window.hide()

    def exibir(self):
        self.window.un_hide()