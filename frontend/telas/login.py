import PySimpleGUI as sg

class TelaLogin:
    """Classe responsável pela Janela de Login."""
    def __init__(self):
        sg.theme("DarkBlue3")
       
        layout = [[
                       sg.Text( "Sistema de Parqueamento",
                           font=("Helvetica", 16, "bold"),
                           justification="center",
                           expand_x=True,)
                   ],
                   [sg.HSeparator()],
                   [sg.Text("Telefone:", size=(10, 1)),
                       sg.Input(key="-LOGIN-TEL-", size=(25, 1)),
                   ],
                   [sg.Text("Senha:", size=(10, 1)),
                       sg.Input(key="-LOGIN-SENHA-", password_char="*", size=(25, 1)),
                   ],
                   [ sg.Button("Entrar", key="-BTN-LOGIN-", bind_return_key=True),
                    sg.Button("Criar Conta", key="-BTN-TELA-CADASTRO-"),
                   ],
          ]
       
        self.window=sg.Window(
                   "Autenticação - Cliente CORBA",
                   layout,
                   element_justification="c",
                   finalize=True,
               )


    def fechar(self):
        self.window.close()

    def ocultar(self):
        self.window.hide()

    def exibir(self):
        self.window.un_hide()
    

        

        
        
        
        

      
