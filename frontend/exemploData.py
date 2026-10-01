import PySimpleGUI as sg

# Define o tema da interface
sg.theme('LightBlue3')

# Layout da janela
layout = [
    [sg.Text('Selecione o período de reserva:', font=('Helvetica', 12, 'bold'))],
    
    # Campo para Data de Entrada
    [
        sg.Text('Data de Entrada:', size=(15, 1)),
        sg.Input(key='-ENTRADA-', size=(15, 1), readonly=True),
        sg.CalendarButton(
            'Escolher Data',
            target='-ENTRADA-',
            format='%Y-%m-%d',
            button_color=('white', '#1f77b4'),
            title='Selecione a Data de Entrada'
        )
    ],
    
    # Campo para Data de Saída
    [
        sg.Text('Data de Saída:', size=(15, 1)),
        sg.Input(key='-SAIDA-', size=(15, 1), readonly=True),
        sg.CalendarButton(
            'Escolher Data',
            target='-SAIDA-',
            format='%Y-%m-%d',
            button_color=('white', '#1f77b4'),
            title='Selecione a Data de Saída'
        )
    ],
    
    [sg.HSeparator()],
    [sg.Button('Confirmar'), sg.Button('Sair')],
    [sg.Text('', key='-RESULTADO-', size=(40, 2), text_color='green')]
]

# Criação da Janela
window = sg.Window('Sistema de Reservas - Seleção de Datas', layout)

# Event Loop (Loop de Eventos)
while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
        
    if event == 'Confirmar':
        data_entrada = values['-ENTRADA-']
        data_saida = values['-SAIDA-']
        
        # Validação simples
        if not data_entrada or not data_saida:
            window['-RESULTADO-'].update('Por favor, selecione ambas as datas.', text_color='red')
        elif data_entrada >= data_saida:
            window['-RESULTADO-'].update('Erro: A data de saída deve ser posterior à data de entrada.', text_color='red')
        else:
            window['-RESULTADO-'].update(
                f'Reserva Confirmada!\nEntrada: {data_entrada} | Saída: {data_saida}',
                text_color='green'
            )

window.close()