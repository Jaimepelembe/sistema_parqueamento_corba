from datetime import datetime

def verificarStatusReserva(data_saida:str,hora_saida:str)->bool:
    """"Verifica o Status da reserva. Caso tenha expirado retorna False caso contrário retorna True"""
    
    formatoDateTime="%d-%m-%Y %H:%M:%S"
    dataHoje=datetime.now()
    stringData=f"{data_saida} {hora_saida}"
    dataFimReserva=datetime.strptime(stringData,formatoDateTime)
    
    if dataHoje> dataFimReserva:
        return False
    else: 
        return True

#print(verificarStatusReserva("14-10-2026","17:00:00"))