from ParqueamentoApp__POA import Observador

# O cliente implementa a interface Observador; é o servidor que a chama
class ObservadorImpl(Observador):
    def __init__(self,janelaAdmin):
        #self.valorActualizado=None
        self.janelaAdmin=janelaAdmin
    
    def notificarParquesActualizados(self,parquesActualizados):
        if self.janelaAdmin:
            print(f"\n>>> Valor actualizado: {parquesActualizados}")
            self.janelaAdmin.write_event_value("-TABELA-PARQUE-ACTUALIZADA-", parquesActualizados)