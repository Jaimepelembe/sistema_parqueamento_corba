import PySimpleGUI as sg
from marcasModelosCarro import dicionarioMarcasModelos

# Define o tema do PySimpleGUI
sg.theme('DarkBlue3')


class TelaAdministrador:
    def __init__(self,usuario_logado,listaParques):
        self.usuario_logado= usuario_logado
        self.lista_parques =listaParques

        
        self.iniciar_janela_principal()



    # --- MONTAGEM DAS TABS PRINCIPAIS ---

    def _criar_tab_parques(self):
        headings = ['Nome', 'Província', 'Localização', 'Telefone', 'Horário', 'Cobertura', 'Preço (MT)']
        provincias_mocambique = ["Maputo","Gaza","Inhambane","Sofala","Manica","Tete","Zambézia","Nampula","Niassa","Cabo Delgado"
]

        return [
            [sg.Text('Adicionar Parque', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome:    '), sg.Input(default_text=self.usuario_logado.nome, key='-PARQUE_NOME-', size=(30, 1))],
            [sg.Text('Provincia:    '), sg.Combo(provincias_mocambique, default_value=provincias_mocambique[0], key='-COMBO-PROVINCIA-', readonly=True, size=(5, 1))],
            [sg.Text('Localização:    '), sg.Input(default_text="", key='-PARQUE_LOCALIZACAO-', size=(30, 1))],
            [sg.Text('Telefone:'), sg.Input(default_text="", key='-PARQUE_TEL-', size=(30, 1))],
            [sg.Text('Horário:   '), sg.Input(default_text="", key='-PARQUE_HORARIO-', size=(30, 1))],
            [sg.Text('Cobertura:    '), sg.Combo(["COBERTO","NAO_COBERTO"], default_value=provincias_mocambique[0], key='-COMBO-COBERTURA-', readonly=True, size=(5, 1))],
            [sg.Text('Preço (MT):    '), sg.Input(default_text="", key='-PARQUE_PRECO-', size=(30, 1))],
            [sg.Button('Adicionar', key='-BTN_ADICIONAR_PARQUE-'),sg.Button('Atualizar Dados', key='-BTN_ATUALIZAR_PARQUE-',disabled=True)],
            
            [sg.HSeparator()],
        
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
            [sg.Text('Clique em uma linha da tabela para actualizar os dados do parque.', font=('Helvetica', 9, 'italic'))],
        ]

    def _criar_tab_perfil(self):
        return [
            [sg.Text('Atualizar Meus Dados', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome:    '), sg.Input(default_text=self.usuario_logado.nome, key='-PERFIL_NOME-', size=(30, 1))],
            [sg.Text('Telefone:'), sg.Input(default_text=self.usuario_logado.telefone, key='-PERFIL_TEL-', size=(30, 1))],
            [sg.Text('Senha:   '), sg.Input(default_text=self.usuario_logado.senha, password_char='*', key='-PERFIL_SENHA-', size=(30, 1))],
            [sg.Button('Atualizar Dados', key='-BTN_ATUALIZAR_PERFIL-')],
        ]


    def iniciar_janela_principal(self):
        layout = [
            [
                sg.TabGroup([
                    [
                        sg.Tab('Parques', self._criar_tab_parques()),
                        sg.Tab('Meu Perfil', self._criar_tab_perfil()),
                      
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

