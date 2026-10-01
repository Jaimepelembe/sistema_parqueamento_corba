import os
import PySimpleGUI as sg


class PainelUsuarioComum:
    def __init__(self, usuario_logado: str):
        self.usuario_logado = usuario_logado
        sg.theme('DarkBlue3')

        # --- ABA 1: Vagas Disponíveis ---
        layout_vagas = [
            [sg.Text('Vagas Livres no Estacionamento', font=('Helvetica', 12, 'bold'))],
            [
                sg.Table(
                    values=[
                        ['A-01', 'Piso 1 - Coberto', 'Livre'],
                        ['A-02', 'Piso 1 - Coberto', 'Livre'],
                        ['B-05', 'Piso 2 - Descoberto', 'Livre'],
                    ],
                    headings=['Código Vaga', 'Localização', 'Estado'],
                    auto_size_columns=True,
                    num_rows=6,
                    key='-TABELA_VAGAS-',
                    enable_events=True,
                )
            ],
            [sg.Button('Reservar Vaga Selecionada', key='-BTN_RESERVAR-')],
        ]

        # --- ABA 2: Registro de Viaturas (Com Foto) ---
        layout_viaturas = [
            [sg.Text('Cadastrar Nova Viatura', font=('Helvetica', 12, 'bold'))],
            [
                sg.Column([
                    [sg.Text('Matrícula:'), sg.Input(key='-MATRICULA-', size=(20, 1))],
                    [sg.Text('Marca/Modelo:'), sg.Input(key='-MODELO-', size=(20, 1))],
                    [
                        sg.Text('Foto do Veículo:'),
                        sg.Input(key='-FOTO_PATH-', enable_events=True, size=(15, 1)),
                        sg.FileBrowse('Procurar', file_types=(("Imagens PNG/GIF", "*.png;*.gif"),)),
                    ],
                    [sg.Button('Salvar Viatura', key='-SALVAR_VIATURA-')],
                ]),
                sg.VSeparator(),
                sg.Column([
                    [sg.Text('Visualização da Foto:')],
                    # Elemento sg.Image exibe a foto do veículo selecionado
                    [sg.Image(key='-PREVIEW_FOTO-', size=(150, 150))],
                ]),
            ],
            [sg.HSeparator()],
            [sg.Text('Minhas Viaturas Cadastradas:')],
            [
                sg.Table(
                    values=[['AB-123-MC', 'Toyota Ractis']],
                    headings=['Matrícula', 'Modelo'],
                    key='-TABELA_VIATURAS-',
                    auto_size_columns=True,
                    num_rows=4,
                )
            ],
        ]

        # --- ABA 3: Perfil do Usuário ---
        layout_perfil = [
            [sg.Text('Meus Dados Cadastrais', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome Completo:'), sg.Input(default_text=self.usuario_logado, key='-NOME_PERFIL-')],
            [sg.Text('Telefone:'), sg.Input(default_text='841234567', key='-TEL_PERFIL-')],
            [sg.Button('Atualizar Meus Dados', key='-ATUALIZAR_PERFIL-')],
        ]

        # Estrutura principal com TabGroup
        layout_principal = [
            [
                sg.TabGroup([
                    [
                        sg.Tab('Vagas & Reservas', layout_vagas),
                        sg.Tab('Minhas Viaturas', layout_viaturas),
                        sg.Tab('Meu Perfil', layout_perfil),
                    ]
                ])
            ],
            [sg.Button('Sair do Sistema', key='-SAIR-')],
        ]

        self.window = sg.Window(f'Painel do Usuário - {self.usuario_logado}', layout_principal, finalize=True)

    def executar(self):
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, '-SAIR-'):
                break

            # Atualizar pré-visualização da foto da viatura ao selecionar um ficheiro
            if event == '-FOTO_PATH-':
                caminho_foto = values['-FOTO_PATH-']
                if caminho_foto and os.path.exists(caminho_foto):
                    try:
                        self.window['-PREVIEW_FOTO-'].update(filename=caminho_foto)
                    except Exception as e:
                        sg.popup_error('O PySimpleGUI nativo requer formato PNG ou GIF para o elemento sg.Image.')

            # Reservar vaga
            if event == '-BTN_RESERVAR-':
                linhas_selecionadas = values['-TABELA_VAGAS-']
                if linhas_selecionadas:
                    sg.popup_ok('Vaga reservada com sucesso para a sua viatura principal!')
                else:
                    sg.popup_error('Selecione uma vaga na tabela primeiro.')

            # Salvar Viatura
            if event == '-SALVAR_VIATURA-':
                matricula = values['-MATRICULA-'].strip()
                modelo = values['-MODELO-'].strip()
                if matricula and modelo:
                    sg.popup('Sucesso', f'Viatura {matricula} cadastrada com sucesso!')
                else:
                    sg.popup_error('Preencha os campos obrigatórios.')

        self.window.close()


if __name__ == '__main__':
    app = PainelUsuarioComum('João Silva')
    app.executar()