from ParqueamentoApp__POA import Observador

# O cliente implementa a interface Observador; é o servidor que a chama
class ObservadorParqueamentoImpl(Observador):
    def __init__(self):
        #self.valorActualizado=None
        self.janelaAdmin=None
        self.janelaUsuarioComum=None
        self.janelaReservaVaga=None
    
    def notificarParquesActualizados(self,parquesActualizados):
        if self.janelaAdmin:
            #print(f"\n>>> Valor actualizado: {parquesActualizados}")
            self.janelaAdmin.write_event_value("-TABELA-PARQUE-ACTUALIZADA-", parquesActualizados)
            
        if self.janelaUsuarioComum:
            self.janelaUsuarioComum.write_event_value("-TABELA-PARQUE-ACTUALIZADA-", parquesActualizados)
    
    def notificarActualizacaoDadosUsuario(self,usuario):
        if self.janelaAdmin:
            #print(f"\n>>> Valor actualizado: {parquesActualizados}")
            self.janelaAdmin.write_event_value("-ATUALIZAR_PERFIL_UM_USUARIO-", usuario)
            
        if self.janelaUsuarioComum:
            self.janelaUsuarioComum.write_event_value("-ATUALIZAR_PERFIL_UM_USUARIO-", usuario)
    
    def notificarActualizacaoVaga(self,listaVagas):
        if self.janelaReservaVaga:
            self.janelaReservaVaga.write_event_value("-ATUALIZAR_VAGAS_DISPONIVEIS-", listaVagas)
        
    def notificarActualizacaoViaturas(self,listaViaturas):
        if self.janelaUsuarioComum:
            self.janelaUsuarioComum.write_event_value("-ATUALIZAR_VIATURAS_DISPONIVEIS-", listaViaturas)
   
    def notificarActualizacaoReservas(self,listaReservas):
        if self.janelaUsuarioComum:
            self.janelaUsuarioComum.write_event_value("-ATUALIZAR_TABELA_RESERVAS-", listaReservas)
            
    
            