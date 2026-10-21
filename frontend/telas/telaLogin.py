import PySimpleGUI as sg

from telas.temaInterface import *
# ----------------------------------------------------------------------
# Paleta e fontes
# ----------------------------------------------------------------------

CARD = PANEL


class TelaLogin:

    def __init__(self):
        
        aplicar_tema()
        self.window=self.criar_janela()


        
    def logo(self,tamanho=84):
        """Ícone redondo com a letra P (desenhado, sem precisar de arquivo)."""
        g = sg.Graph((tamanho, tamanho), (0, 0), (tamanho, tamanho),
                    background_color=CARD, key="-LOGO-", pad=(0, 0))
        return g


    def desenhar_logo(self,graph, tamanho=84):
        graph.draw_circle((tamanho / 2, tamanho / 2), tamanho / 2 - 2,
                        fill_color=ACENTO, line_color="#7FA8F5", line_width=3)
        graph.draw_text("P", (tamanho / 2, tamanho / 2 - 2), color="white",
                        font=(FONTE, 40, "bold"))


    def campo(self,rotulo, chave, senha=False):
        coluna = [
            [sg.Text(rotulo, font=F_LABEL, text_color=TEXTO_SEC,
                    background_color=CARD, pad=(0, (14, 4)))],
            [sg.Input(key=chave, size=(29, 1),
                    password_char="●" if senha else "",
                    pad=(0, 0), **{**CAMPO, "font": (FONTE, 15)})],
        ]
        return [[sg.Column(coluna, background_color=CARD, pad=(0, 0),
                        element_justification="l")]]


    def criar_layout(self):
        cartao = [
            [sg.Text("", background_color=CARD, pad=(0, 10))],
            [sg.Push(background_color=CARD), self.logo(), sg.Push(background_color=CARD)],
            [sg.Push(background_color=CARD),
            sg.Text("Sistema de Parqueamento", font=F_TITULO, text_color=TEXTO,
                    background_color=CARD, pad=(0, (10, 0))),
            sg.Push(background_color=CARD)],
            [sg.Push(background_color=CARD),
            sg.Text("Entre com o seu telefone e senha", font=F_SUB,
                    text_color=TEXTO_SEC, background_color=CARD, pad=(0, (2, 8))),
            sg.Push(background_color=CARD)],
            [sg.HorizontalSeparator(color=LINHA, pad=(50, 6))],
            *self.campo("TELEFONE", "-LOGIN-TEL-"),
            *self.campo("SENHA", "-LOGIN-SENHA-", senha=True),
            [sg.Push(background_color=CARD),
            sg.Button("ENTRAR", key="-BTN-LOGIN-", size=(13, 1), pad=((0, 4), (30, 10)), **{**BTN_PRIMARIO, "font": (FONTE, 13, "bold")}),
            sg.Button("CRIAR CONTA", key="-BTN-TELA-CADASTRO-", size=(13, 1), pad=((4, 0), (30, 10)), **{**BTN_SECUNDARIO, "font": (FONTE, 13, "bold")}),
            sg.Push(background_color=CARD)],
            [sg.Text("", background_color=CARD, pad=(0, 6))],
        ]

        return [
            [sg.VPush(background_color=BG)],
            [sg.Push(background_color=BG),
            sg.Column(cartao, background_color=CARD, pad=(0, 0), element_justification="c"),
            sg.Push(background_color=BG)],
            [sg.VPush(background_color=BG)],
            [sg.Push(background_color=BG),
            sg.Text("© Sistema de Parqueamento", font=F_RODAPE, text_color=TEXTO_SEC,
                    background_color=BG, pad=(0, (0, 8))),
            sg.Push(background_color=BG)],
        ]


    def criar_janela(self):
        janela = sg.Window("Autenticação - Cliente", self.criar_layout(),
                        size=(600, 700), background_color=BG,
                        finalize=True, element_justification="c")
        self.desenhar_logo(janela["-LOGO-"])
        janela["-LOGIN-TEL-"].set_focus()
        return janela
    
    
    def fechar(self):
        self.window.close()

    def ocultar(self):
        self.window.hide()

    def exibir(self):
        self.window.un_hide()
