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


class TelaPrincipal:
    """Classe responsável pelo Menu Principal."""
    def __init__(self, usuario: str):
        sg.theme('DarkBlue3')
        layout = [
            [sg.Text(f'Bem-vindo(a), {usuario}!', font=('Helvetica', 14))],
            [sg.Button('Abrir Cadastro', size=(20, 2))],
            [sg.Button('Fazer Logout', size=(20, 1)), sg.Button('Sair', size=(10, 1))]
        ]
        self.window = sg.Window('Sistema - Menu Principal', layout, finalize=True)

    def fechar(self):
        self.window.close()

    def ocultar(self):
        self.window.hide()

    def exibir(self):
        self.window.un_hide()


class TelaCadastro:
    """Classe responsável pela Janela de Cadastros."""
    def __init__(self):
        sg.theme('DarkBlue3')
        layout = [
            [sg.Text('Cadastro de Usuário', font=('Helvetica', 14))],
            [sg.Text('Nome Completo:'), sg.Input(key='-NOME-', size=(30, 1))],
            [sg.Text('Perfil:       '), sg.Combo(['Administrador', 'Operador'], default_value='Operador', key='-PERFIL-')],
            [sg.Button('Salvar'), sg.Button('Voltar')]
        ]
        self.window = sg.Window('Cadastro', layout, finalize=True)

    def fechar(self):
        self.window.close()


class GerenciadorJanelas:
    """Classe controladora que gerencia a transição entre telas e eventos."""
    def __init__(self):
        self.tela_login = TelaLogin()
        self.tela_principal = None
        self.tela_cadastro = None

    def executar(self):
        while True:
            # Captura eventos de TODAS as janelas abertas
            window, event, values = sg.read_all_windows()

            # --- EVENTOS DA TELA DE LOGIN ---
            if window == self.tela_login.window:
                if event in (sg.WIN_CLOSED, 'Sair'):
                    break
                
                elif event == 'Entrar':
                    usuario = values['-USUARIO-'].strip()
                    senha = values['-SENHA-'].strip()

                    if usuario and senha:  # Validação simples
                        self.tela_login.ocultar()
                        self.tela_principal = TelaPrincipal(usuario)
                    else:
                        sg.popup_error('Por favor, preencha usuário e senha.')

            # --- EVENTOS DA TELA PRINCIPAL ---
            elif self.tela_principal and window == self.tela_principal.window:
                if event in (sg.WIN_CLOSED, 'Sair'):
                    break

                elif event == 'Abrir Cadastro':
                    if self.tela_cadastro is None:
                        self.tela_principal.ocultar()
                        self.tela_cadastro = TelaCadastro()

                elif event == 'Fazer Logout':
                    self.tela_principal.fechar()
                    self.tela_principal = None
                    self.tela_login.exibir()

            # --- EVENTOS DA TELA DE CADASTRO ---
            elif self.tela_cadastro and window == self.tela_cadastro.window:
                if event == sg.WIN_CLOSED or event == 'Voltar':
                    self.tela_cadastro.fechar()
                    self.tela_cadastro = None
                    self.tela_principal.exibir()

                elif event == 'Salvar':
                    nome = values['-NOME-']
                    perfil = values['-PERFIL-']
                    if nome:
                        sg.popup(f'Usuário "{nome}" ({perfil}) cadastrado com sucesso!')
                        self.tela_cadastro.fechar()
                        self.tela_cadastro = None
                        self.tela_principal.exibir()
                        
                    else:
                        sg.popup_error('O nome não pode estar em branco.')

        # Encerra qualquer janela aberta ao fechar a aplicação
        self.encerrar_aplicacao()

    def encerrar_aplicacao(self):
        if self.tela_login:
            self.tela_login.fechar()
        if self.tela_principal:
            self.tela_principal.fechar()
        if self.tela_cadastro:
            self.tela_cadastro.fechar()


if __name__ == '__main__':
    app = GerenciadorJanelas()
    app.executar()