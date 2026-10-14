import schedule
import time

# A sua lista de dados
minha_lista = [10, 20, 30, 45, 50]

def verificar_condicao(item):
    # Defina aqui a sua condição (exemplo: se o valor for maior que 40)
    return item > 40

def executar_acao(item):
    # Defina aqui a ação que deve acontecer
    print(f" Alerta! Condição satisfeita para o item: {item}")

def tarefa_agendada():
    print("A verificar a lista...")
    
    # Percorre a lista para verificar a condição
    for elemento in minha_lista:
        if verificar_condicao(elemento):
            executar_acao(elemento)

# Agenda a função para rodar de 5 em 5 minutos
schedule.every(1).minutes.do(tarefa_agendada)

# Executa a tarefa uma vez logo no início (opcional)
tarefa_agendada()

# Loop infinito para manter o script a correr e verificar o relógio
while True:
    schedule.run_pending()
    time.sleep(1)  # Espera 1 segundo entre as verificações do relógio
    #print("Hello")
