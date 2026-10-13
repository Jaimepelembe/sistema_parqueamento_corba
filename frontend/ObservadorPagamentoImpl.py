from PagamentoApp__POA import Observador

# O cliente implementa a interface Observador; é o servidor que a chama
class ObservadorPagamentoImpl(Observador):
    def __init__(self):
        #self.valorActualizado=None
        self.janelaUsuarioComum=None
     
    
   
    def notificarActualizacaoSaldo(self,saldo):
        if self.janelaUsuarioComum:
            self.janelaUsuarioComum.write_event_value("-ATUALIZAR_SALDO_UM_USUARIO-", saldo)
    
    
    def notificarActualizacaoTransacao(self,listaTransacoes):
        import PySimpleGUI as sg
        if self.janelaUsuarioComum:
            self.janelaUsuarioComum.write_event_value("-ATUALIZAR_TABELA_TRANSACOES-", listaTransacoes)
            
    
            