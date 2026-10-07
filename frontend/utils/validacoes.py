import re
import PySimpleGUI as sg

# Define o tema do PySimpleGUI
sg.theme('DarkBlue3')


def validarSenha2(senha: str) -> bool:
    """
    Valida a senha com base nos critérios:
    - Mínimo de 8 caracteres
    - Pelo menos 1 letra maiúscula
    - Pelo menos 1 letra minúscula
    - Pelo menos 1 número
    - Pelo menos 1 caractere especial (@, #, $, %, etc.)
    """
    if len(senha) < 8:
        sg.popup_error('Senha Inválida', 'A senha deve ter pelo menos 8 caracteres.', title='Erro')
        return False
    if not re.search(r'[A-Z]', senha):
        sg.popup_error('Senha Inválida', 'A senha deve conter pelo menos uma letra maiúscula.', title='Erro')
        return False
    if not re.search(r'[a-z]', senha):
        sg.popup_error('Senha Inválida', 'A senha deve conter pelo menos uma letra minúscula.', title='Erro')
        return False
    if not re.search(r'\d', senha):
        sg.popup_error('Senha Inválida', 'A senha deve conter pelo menos um número.', title='Erro')
        return False
    if not re.search(r'[@$!%*?&._\-#]', senha):
        sg.popup_error('Senha Inválida', 'A senha deve conter pelo menos um caractere especial (@, #, $, %, etc.).', title='Erro')
        return False

    return True




def validarSenha(senha: str) -> bool:
    """
    Valida se a senha possui pelo menos 4 caracteres.
    Exibe um pop-up de erro via PySimpleGUI caso a validação falhe.
    """
    if len(senha) < 4:
        sg.popup_error(
            'Senha Inválida',
            'A senha deve ter pelo menos 4 caracteres.',
            title='Erro de Validação'
        )
        return False
        
    return True

def validarNome(nome: str) -> bool:
    """
    Valida se o nome possui pelo menos 4 caracteres.
    Exibe um pop-up de erro via PySimpleGUI caso a validação falhe.
    """
    if len(nome) < 2:
        sg.popup_error(
            'Nome Inválida',
            'O nome deve ter pelo menos 3 caracteres.',
            title='Erro de Validação'
        )
        return False
        
    return True



def validarTelefone(telefone: str) -> bool:
    """
    Valida número de telefone (aceita formato Moçambique/Internacional ou padrão genérico com DDD).
    Exemplos válidos:
    - Moçambique: 841234567, 821234567, 861234567, +258841234567
    - Padrão Genérico: (11) 98765-4321 ou apenas 9 a 13 dígitos numéricos.
    """
    # Remove espaços, traços e parênteses para analisar apenas dígitos e o sinal de +
    apenas_digitos = re.sub(r'[^\d+]', '', telefone)

    if not apenas_digitos:
        sg.popup_error('Telefone Inválido', 'O campo telefone não pode estar vazio.', title='Erro')
        return False

    # Regex que aceita formatos comuns com 9 a 13 dígitos (com ou sem código de país +)
    padrao_telefone = r'^\+?\d{9,13}$'

    if not re.match(padrao_telefone, apenas_digitos):
        sg.popup_error(
            'Telefone Inválido',
            'Informe um número válido contendo entre 9 e 13 dígitos.\nExemplo: 841234567 ou +258841234567',
            title='Erro'
        )
        return False

    return True


def validar_dinheiro_string(valor):
    # Expressão regular para formatos comuns de moeda (com ou sem separadores de milhares)
    padrao = r'^\d+([.,]\d{1,2})?$'
    return bool(re.match(padrao, valor.strip()))

def validar_dinheiro(valor) ->float:
    valor = valor.strip().replace(",", ".")

    try:
        numero = float(valor)
        return numero 
    except ValueError:
        return False
    
def validarMatricula(matricula:str):
    padrao=r"^[A-Z]{3}\s\d{3}\s(MP|MC|GZ|IB|SF|MN|TT|ZB|NP|NS|CA){1}$"
    resultado= bool(re.match(padrao, matricula))
    if not resultado:
        sg.popup_error(
            'Marca Inválida',
            'A marca deve estar no formato 3 Letras 3 Digitos e o indicativo da provincia\nExemplo: ABC 123 MP.',
            title='Erro de Validação'
        )
    return resultado
        
    
"""
testes = [
    "ABC 123 MC",      # Válido
    "xyz 789 vermelho",  # Válido
    "A1C 123 azul",      # Inválido (contém número nas três letras)
    "ABC 126 MP",       # Inválido (falta um dígito)
    "XYZ 789 amarelo"    # Inválido (amarelo não está na lista de opções)
]


for item in testes:
    print(f"{item}: {validarMatricula(item)}")


# Exemplos de uso:
print(validar_dinheiro_string("1250.50"))   # True
print(validar_dinheiro_string("1,250.50"))  # True
print(validar_dinheiro_string("1250"))      # True (aceita sem cêntimos)
print(validar_dinheiro_string("12,50,50"))  # False (formato inválido)
print(validar_dinheiro_string("abc"))      # False

print(validar_dinheiro("12450.0"))

"""

#print(validarSenha("12345Ae!"))
#print(validarTelefone("847502352"))
#print("Ola mundo")

