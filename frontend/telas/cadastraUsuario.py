import PySimpleGUI as sg

class TelaCadastroUsuario:
    """Classe responsável pela Janela de Cadastro do usuario."""
    def __init__(self):
        sg.theme("DarkBlue3")
       
        layout =   [
                 [sg.Text("Nome:"),sg.Input(key="-CAD-NOME-", size=(25, 1)),],
                 [sg.Text("Telefone:"), sg.Input(key="-CAD-TEL-", size=(25, 1)),],
                    [sg.Text("Senha:"), sg.Input(key="-CAD-SENHA-",password_char="*",size=(25, 1),),],
                     [sg.Button("Registar Utilizador", key="-BTN-CAD-USER-")
                                ],
                            ],
       
        self.window=sg.Window("Autenticação - Cliente CORBA", layout,element_justification="c",finalize=True,)


    def fechar(self):
        self.window.close()

    def ocultar(self):
        self.window.hide()

    def exibir(self):
        self.window.un_hide()
    

        

        
        
    

          
  
                

     