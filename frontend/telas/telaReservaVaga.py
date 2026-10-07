import PySimpleGUI as sg


class TelaReservaVaga:
    
    def __init__(self, minhasMatriculas, parqueSelecioinado,vagasDisponiveis):
        
        self.listaMatriculas=minhasMatriculas
        self.parque_selecionado=parqueSelecioinado
        self.vagas_disponiveis=vagasDisponiveis

        # Gerar opções de horas (00 a 23) e minutos (00, 15, 30, 45)
        horas = [f'{h:02d}' for h in range(24)]
        minutos = ['00', '15', '30', '45']

        layout_reserva = [
            [sg.Text(f'Reservar Vaga - {self.parque_selecionado.nome}', font=('Helvetica', 13, 'bold'))],
            [sg.Text(f'Preço por Hora: {self.parque_selecionado.preco:.2f} MT')],
            [
                sg.Text('Selecionar Vaga:    '),
                sg.Combo(
                    self.vagas_disponiveis,
                    default_value=self.vagas_disponiveis[0] if self.vagas_disponiveis else '',
                    key='-COMBO-VAGA-',
                    readonly=True,
                    size=(20, 1),
                ),
            ],
            [
                sg.Text('Selecionar Viatura:'),
                sg.Combo(
                    self.listaMatriculas,
                    default_value=self.listaMatriculas[0] if self.listaMatriculas else '',
                    key='-COMBO-MATRICULA-',
                    readonly=True,
                    size=(20, 1),
                ),
            ],
            
                  # Campo para Data de Entrada
       [
           sg.Text('Data de Entrada:', size=(15, 1)),
           sg.Input(key='-DT-ENTRADA-', size=(15, 1), readonly=True),
          sg.Button('Escolher Data', key='-BTN-DATA-ENTRADA-')
        
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
           sg.Button('Escolher Data', key='-BTN-DATA-SAIDA-')
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

        self.window= sg.Window('Efetuar Reserva', layout_reserva, finalize=True)


    def fechar(self):
        self.window.close()

    def ocultar(self):
        self.window.hide()

    def exibir(self):
        self.window.un_hide()
        
        