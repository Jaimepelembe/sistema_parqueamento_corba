"""
Tema compartilhado do Sistema de Parqueamento.

Uso em qualquer tela:
    from tema_parqueamento import *
    aplicar_tema()
    sg.Button("Adicionar", **BTN_PRIMARIO)
    sg.Table(..., **TABELA)
"""
import PySimpleGUI as sg

# ----------------------------------------------------------------------
# Paleta (todas as combinações texto/fundo têm contraste >= 4.5:1)
# ----------------------------------------------------------------------
BG         = "#14213A"   # fundo das janelas
PANEL      = "#1D3050"   # cartões, abas, áreas agrupadas
LINHA      = "#3B5278"   # separadores e bordas
TEXTO      = "#F5F8FC"   # texto principal
TEXTO_SEC  = "#C2CEE0"   # rótulos e dicas
CAMPO_BG   = "#F5F8FC"   # fundo dos campos de entrada
CAMPO_TX   = "#0E1A2E"   # texto dentro dos campos

ACENTO     = "#2563EB"   # ação principal
ACENTO_HV  = "#1D4ED8"
SECUNDARIO = "#3B5278"
SECUND_HV  = "#4A6590"
PERIGO     = "#C53030"
PERIGO_HV  = "#A82727"
SUCESSO    = "#15803D"
SUCESSO_HV = "#116A33"
DESATIVADO = ("#9FB0C8", "#27395A")      # (texto, fundo) de botão desativado

# Tabela: fundo claro com texto escuro para máxima leitura dos dados
TAB_LINHA_1 = "#FFFFFF"
TAB_LINHA_2 = "#E8EFF9"
TAB_TEXTO   = "#0E1A2E"
TAB_CAB_BG  = "#0F3D91"
TAB_CAB_TX  = "#FFFFFF"
TAB_SEL_BG  = "#2563EB"
TAB_SEL_TX  = "#FFFFFF"

# ----------------------------------------------------------------------
# Fontes
# ----------------------------------------------------------------------
FONTE      = "Segoe UI"
F_TITULO   = (FONTE, 26, "bold")
F_SECAO    = (FONTE, 13, "bold")
F_SUB      = (FONTE, 12)
F_LABEL    = (FONTE, 11, "bold")
F_TEXTO    = (FONTE, 11)
F_CAMPO    = (FONTE, 12)
F_BOTAO    = (FONTE, 11, "bold")
F_TABELA   = (FONTE, 11)
F_RODAPE   = (FONTE, 9)

# ----------------------------------------------------------------------
# Estilos prontos (use com **)
# ----------------------------------------------------------------------
_BASE_BTN = dict(font=F_BOTAO, border_width=0, disabled_button_color=(DESATIVADO[0], DESATIVADO[1]))
BTN_PRIMARIO   = dict(_BASE_BTN, button_color=("white", ACENTO),     mouseover_colors=("white", ACENTO_HV))
BTN_SECUNDARIO = dict(_BASE_BTN, button_color=("white", SECUNDARIO), mouseover_colors=("white", SECUND_HV))
BTN_PERIGO     = dict(_BASE_BTN, button_color=("white", PERIGO),     mouseover_colors=("white", PERIGO_HV))
BTN_SUCESSO    = dict(_BASE_BTN, button_color=("white", SUCESSO),    mouseover_colors=("white", SUCESSO_HV))

CAMPO = dict(font=F_CAMPO, background_color=CAMPO_BG, text_color=CAMPO_TX, border_width=0)

COMBO = dict(font=F_CAMPO, background_color=CAMPO_BG, text_color=CAMPO_TX,
             button_background_color=ACENTO, button_arrow_color="white", readonly=True)

TABELA = dict(
    font=F_TABELA, text_color=TAB_TEXTO, background_color=TAB_LINHA_1,
    alternating_row_color=TAB_LINHA_2,
    header_font=(FONTE, 11, "bold"),
    header_text_color=TAB_CAB_TX, header_background_color=TAB_CAB_BG,
    selected_row_colors=(TAB_SEL_TX, TAB_SEL_BG),
    row_height=26, border_width=0, header_border_width=0,
    sbar_background_color=SECUNDARIO, sbar_arrow_color="white", sbar_trough_color=PANEL,
)

TABGROUP = dict(
    font=F_LABEL, title_color=TEXTO_SEC, background_color=BG,
    tab_background_color=PANEL, selected_title_color="white",
    selected_background_color=ACENTO, tab_border_width=0, border_width=0,
)

ABA = dict(background_color=PANEL, title_color=TEXTO_SEC)


def aplicar_tema():
    """Registra e ativa o tema 'Parque' (equivalente a sg.theme('DarkBlue3'))."""
    sg.theme_add_new("Parque", {
        "BACKGROUND": BG, "TEXT": TEXTO,
        "INPUT": CAMPO_BG, "TEXT_INPUT": CAMPO_TX,
        "SCROLL": SECUNDARIO, "BUTTON": ("white", ACENTO),
        "PROGRESS": (ACENTO, PANEL),
        "BORDER": 0, "SLIDER_DEPTH": 0, "PROGRESS_DEPTH": 0,
    })
    sg.theme("Parque")
    sg.set_options(font=F_TEXTO)
