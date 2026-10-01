import PySimpleGUI as sg

class TelaLogin:
    """Classe responsável pela Janela de Login."""
    def __init__(self):
        sg.theme('DarkBlue3')
        layout = [
            [sg.Text('Acesso ao Sistema', font=('Helvetica', 16))],
            [sg.Text('Usuário:'), sg.Input(key='-USUARIO-', size=(25, 1))],
            [sg.Text('Senha:  '), sg.Input(key='-SENHA-', password_char='*', size=(25, 1))],
            [sg.Button('Entrar', bind_return_key=True), sg.Button('Sair')]
        ]
        self.window = sg.Window('Login', layout, finalize=True)

    def fechar(self):
        self.window.close()

    def ocultar(self):
        self.window.hide()

    def exibir(self):
        self.window.un_hide()