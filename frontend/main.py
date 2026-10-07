import PySimpleGUI as sg
from telas.login import TelaLogin
from telas.TelaPrincipal import TelaPrincipal
from telas.cadastraUsuario import TelaCadastroUsuario
from telas.telaUsuarioComum import TelaUsuarioComum
from telas.telaAdministrador import TelaAdministrador
from telas.telaReservaVaga import TelaReservaVaga

from validacoes import validarSenha
from validacoes import validarTelefone
from validacoes import validarNome
from validacoes import validar_dinheiro_string
from validacoes import validar_dinheiro
from validacoes import validarMatricula

from datetime import datetime
#from datetime import 

#Importacoes de corba
import sys
from omniORB import CORBA
import CosNaming

# Importar o módulo gerado pelo omniidl a partir do IDL
import ParqueamentoApp
import PagamentoApp






class GerenciadorJanelas:
    """Classe controladora que gerencia a transição entre telas e eventos."""
    def __init__(self):
        self.tela_login = TelaLogin()
        self.tela_usuario_comum = None
        self.tela_administrador = None
        self.tela_cadastro = None
        self.tela_reserva_vaga=None
        self.inicializarCORBA()
        self.listaParquesDTO=None
        self.listaVagasDTO=None
        self.listaVagasReservadasDTO=None
        self.listaViaturasDTO=None
        self.listaTransacoesDTO=None
        self.listaReservasVagaDTO=None

        

    def inicializarCORBA(self,initial_host="localhost",initial_port="1050"):
        # Monta o argumento no formato padrão CORBA
        # Exemplo resultante: -ORBInitRef NameService=corbaloc:iiop:192.168.1.50:1050/NameService
        init_ref_arg = f"NameService=corbaname:iiop:{initial_host}:{initial_port}/NameService"

        # Adiciona aos argumentos do sistema que serão lidos pelo ORB
        orb_args = sys.argv + ["-ORBInitRef", init_ref_arg]
        orb = CORBA.ORB_init(orb_args)
        
        naming_service = orb.resolve_initial_references("NameService")
        self.root_context = naming_service._narrow(CosNaming.NamingContext)


        # Resolver as referências das interfaces no NameService
        self.servico_usuario = self.obter_servico(
            "Usuario", ParqueamentoApp.Usuario
        )
        self.servico_parque = self.obter_servico(
            "Parque", ParqueamentoApp.Parque
        )
        self.servico_vaga = self.obter_servico(
            "Vaga", ParqueamentoApp.Vaga
        )
        self.servico_viatura = self.obter_servico(
            "Viatura", ParqueamentoApp.Viatura
        )
        self.servico_reserva = self.obter_servico(
            "Reserva", ParqueamentoApp.Reserva
        )
        
        self.servico_conta= self.obter_servico("Conta",PagamentoApp.Conta)
        self.servico_transacao= self.obter_servico("Transacao",PagamentoApp.Transacao)

        # Guarda o utilizador autenticado após o login
        self.usuario_logado = None
    
    
    
    def obter_servico(self, nome_servico, interface_class):
        name = [CosNaming.NameComponent(nome_servico, "")]
        obj = self.root_context.resolve(name)
        return obj._narrow(interface_class)
        
        
    
    
    def encerrar_aplicacao(self):
        if self.tela_login:
            self.tela_login.fechar()
        if self.tela_usuario_comum:
            self.tela_usuario_comum.fechar()
        if self.tela_cadastro:
            self.tela_cadastro.fechar()
        if self.tela_administrador:
            self.tela_administrador.fechar()
   
    def listarTransacoes(self):
        self.listaTransacoesDTO= self.servico_transacao.listarTransacoes(self.usuario_logado.id_usuario)
        listaTransacoes=[]
        for transacaoDTO in self.listaTransacoesDTO:
            listaTransacoes.append([transacaoDTO.id_transacao,transacaoDTO.tipo,transacaoDTO.valor,transacaoDTO.estado,transacaoDTO.data,transacaoDTO.hora])

        return listaTransacoes
    
    def listarViaturas(self) ->list[ParqueamentoApp.ViaturaDTO]:
        self.listaViaturasDTO=self.servico_viatura.listarViaturas(self.usuario_logado.id_usuario)
        #print(self.listaViaturasDTO)
        
        listaViaturas=[]
        for viaturaDTO in self.listaViaturasDTO:
            listaViaturas.append([viaturaDTO.marca,viaturaDTO.modelo,viaturaDTO.matricula])
        return listaViaturas    
    
    def listarParques(self) ->list:
        self.listaParquesDTO=self.servico_parque.pesquisarPorCategoria("nome")
        listaParques=[]
        for parqueDTO in self.listaParquesDTO:
            listaParques.append([parqueDTO.nome,parqueDTO.provincia,parqueDTO.localizacao,parqueDTO.telefone,parqueDTO.horario,parqueDTO.cobertura,parqueDTO.preco])
            #print(parqueDTO.nome)
        return listaParques
    
    
    def listarVagasDisponiveis(self,id_parque) ->list:
        self.listaVagasDTO=self.servico_vaga.listarVagasDisponiveis(id_parque)
        listaVagas=[]
        for vagaDTO in self.listaVagasDTO:
            listaVagas.append(vagaDTO.numero_vaga)
        return listaVagas
    
    def listarVagasReservadas(self,id_parque) ->list:
        self.listaVagasReservadasDTO=self.servico_vaga.listarVagasReservadas(id_parque)
        listaVagas=[]
        for vagaDTO in self.listaVagasDTO:
            listaVagas.append(vagaDTO.numero_vaga)
        return listaVagas
    
    def buscarNumeroVagaReservada(self,id_vaga):
        """Busca o numero de uma vaga que ja foi reservada pelo usuario. Retorna o numero da vaga"""
        #self.listarVagasDisponiveis()
        numeroVaga=None
        for vagaDTO in self.listaVagasDTO:
            if vagaDTO.id_vaga==id_vaga:
                numeroVaga=vagaDTO.numero_vaga
                break
        return numeroVaga
        
    
    def verificarContaBancaria(self):
        idConta=self.servico_conta.buscarIDConta(self.usuario_logado.id_usuario)
        if idConta>0:
            #print(idConta)
            print("Ja tem conta")
        else:
            print("Nao tem conta.")
            conta =PagamentoApp.ContaDTO(-1,0,self.usuario_logado.id_usuario)
            resultado=self.servico_conta.criarConta(conta) 
            if resultado:
                print("Conta Criada com sucesso")
    
    def actualizarDadosUsuario(self,window,values):
        novoNome=values["-PERFIL_NOME-"]
        novoTelefone=values["-PERFIL_TEL-"]
        novaSenha=values["-PERFIL_SENHA-"]
        
        if validarNome(novoNome) and validarTelefone(novoTelefone) and validarSenha(novaSenha):
            nomeAntigo=self.usuario_logado.nome
            telefoneAntigo=self.usuario_logado.telefone
            senhaAntiga=self.usuario_logado.senha
            if novoNome!=nomeAntigo or novoTelefone!= telefoneAntigo or novaSenha!= senhaAntiga:
                #print("DadosSao diferentes")
                usuarioDTO=ParqueamentoApp.UsuarioDTO(self.usuario_logado.id_usuario,novoNome,novoTelefone,novaSenha,self.usuario_logado.tipo)
                sucesso=self.servico_usuario.actualizarDados(usuarioDTO)
                #self.servico_usuario.login(novoTelefone,novaSenha)
                if sucesso:
                    window["-PERFIL_NOME-"].update(novoNome)
                    window["-PERFIL_TEL-"].update(novoTelefone)
                    window["-PERFIL_SENHA-"].update(novaSenha)
                    
                    sg.popup('Sucesso', 'Dados actualizados com sucesso.')
            else:
                 sg.popup_error('Erro', 'Voce nao modificou nenhum dos seus dados!\nModifique um deles para poder actualizar.')
    
    
    def depositar(self,window,values):
        valorDeposito=values["-VALOR_DEPOSITO-"]
        if valorDeposito!="" and validar_dinheiro_string(valorDeposito):
            valorDeposito=validar_dinheiro(valorDeposito)
        
            foiDepositado=self.servico_conta.depositar(self.usuario_logado.id_usuario,valorDeposito)
            if foiDepositado:
                idConta=self.servico_conta.buscarIDConta(self.usuario_logado.id_usuario)
                if idConta>0:
                    hoje=datetime.now()
                    data=hoje.strftime("%d-%m-%Y")
                    hora=hoje.strftime("%H:%M:%S")
                    transacaoDTO= PagamentoApp.TransacaoDTO(-1,"DEPOSITO",valorDeposito,"CONCLUIDO",data,hora, idConta)
                    sucesso=self.servico_transacao.efetuarTransacao(transacaoDTO)
                    if sucesso:
                        # Actualizar o saldo actual e o historico de transacoes
                        #self.listaTransacoesDTO=self.servico_transacao.listarTransacoes(self.usuario_logado.id_usuario)  
                        self.saldoActual= self.servico_conta.consultarSaldo(self.usuario_logado.id_usuario)
                        window['-TXT_SALDO-'].update(f'Saldo Atual: {self.saldoActual:.2f} MT')        
                        window['-TABELA_TRANSACOES-'].update(values=self.listarTransacoes())        
                        window['-VALOR_DEPOSITO-'].update('')        
                               
                        sg.popup('Sucesso', 'O deposito foi efectuado com sucesso.')
            
        else:
            sg.popup_error('Erro', 'O valor de deposito deve ser maior que zero.')
    

    def debitar(self,window,valorDebito:float):
        if valorDebito and valorDebito>0 :
        
            foiDebitado=self.servico_conta.debitar(self.usuario_logado.id_usuario,valorDebito)
            if foiDebitado:
                idConta=self.servico_conta.buscarIDConta(self.usuario_logado.id_usuario)
                if idConta>0:
                    hoje=datetime.now()
                    data=hoje.strftime("%d-%m-%Y")
                    hora=hoje.strftime("%H:%M:%S")
                    transacaoDTO= PagamentoApp.TransacaoDTO(-1,"DEBITO",valorDebito,"CONCLUIDO",data,hora, idConta)
                    sucesso=self.servico_transacao.efetuarTransacao(transacaoDTO)
                    if sucesso:
                        # Actualizar o saldo actual e o historico de transacoes
                        #self.listaTransacoesDTO=self.servico_transacao.listarTransacoes(self.usuario_logado.id_usuario)  
                        self.saldoActual= self.servico_conta.consultarSaldo(self.usuario_logado.id_usuario)
                        window['-TXT_SALDO-'].update(f'Saldo Atual: {self.saldoActual:.2f} MT')        
                        window['-TABELA_TRANSACOES-'].update(values=self.listarTransacoes())          
                            
                        #Actualizar o historico de reservas
                        window['-TABELA_RESERVAS-'].update(values=self.listarReservasVaga())   
                        
                                
                        #sg.popup('Sucesso', 'O deposito foi efectuado com sucesso.')
                        print(f"Debitou {valorDebito} com sucesso")
            
        else:
            sg.popup_error('Erro', 'O valor de debito deve ser maior que zero.')
    

    def selecionarModelosCarro(self,window,values):
        marca=values["-MARCA-"]
        modelosCarros=self.tela_usuario_comum.dicionarioCarros[marca]

        #Actualizar comboBox dos modelos
        window["-MODELO-"].update(values=modelosCarros,value="")
      
        
        
    def adicionarViatura(self,window,values):
        marca=values["-MARCA-"]
        modelo=values["-MODELO-"]
        matricula=values["-MATRICULA-"]
        
        if len(marca)>1 and len(modelo)>1 and validarMatricula(matricula):
            viaturaDTO = ParqueamentoApp.ViaturaDTO(-1,marca,modelo,matricula,self.usuario_logado.id_usuario)
            self.servico_viatura.adicionarViatura(viaturaDTO)
            window["-TABELA_VIATURAS-"].update(values=self.listarViaturas())
            window["-MARCA-"].update(value="")
            window["-MODELO-"].update(values=[],value="")
            window["-MATRICULA-"].update("Ex: ABC 126 MP")
   
    def listarMatriculaViaturas(self):
        listaMatriculaViaturas=[]
        for viaturaDTO in self.listaViaturasDTO:
            listaMatriculaViaturas.append(viaturaDTO.matricula)
            #print(viaturaDTO.matricula)
        return listaMatriculaViaturas  

    def  buscarMatriculaViaturaReservada(self,id_viatura):
        """Busca o numero de matricula de uma viatura que tem uma reservada feita pelo usuario. Retorna o numero da matricula"""
        matricula=None
        for viaturaDTO in self.listaViaturasDTO:
            if viaturaDTO.id_viatura==id_viatura:
                matricula=viaturaDTO.matricula
                break
        return matricula
        
    

    def escolherData(self,titulo,window,key):
        data = sg.popup_get_date(title=titulo,keep_on_top=True,modal=True)
        mes,dia,ano=data
        dataFormatada=f"{dia:02d}-{mes:02d}-{ano}"
        window[key].update(dataFormatada)
        #print(dataFormatada)
    
    def validarVagaSelecionada(self,values)->int:
        numeroVagaSelecionada=values["-COMBO-VAGA-"]
        id_vaga=-1
        if numeroVagaSelecionada !="" and numeroVagaSelecionada:
            indice=self.tela_reserva_vaga.vagas_disponiveis.index(numeroVagaSelecionada)
            vagaDTO=self.listaVagasDTO[indice]
            id_vaga=vagaDTO.id_vaga
        
        else:
            sg.popup_error('Erro', 'Voce selecionou uma vaga invalida!')
        
        return id_vaga

    def validarMatriculaSelecionada(self,values)->int:    
        matriculaSelecionada=values["-COMBO-MATRICULA-"]
        id_viatura=-1
   
        if matriculaSelecionada !="" and matriculaSelecionada:
            indice=self.tela_reserva_vaga.listaMatriculas.index(matriculaSelecionada)
            viaturaDTO=self.listaViaturasDTO[indice]
            id_viatura=viaturaDTO.id_viatura    
        else:
            sg.popup_error('Erro', 'Voce selecionou uma matricula invalida!')
        
        return id_viatura

    def validarPeriodoEscolhido(self,values):
        dataEntrada= values["-DT-ENTRADA-"]    
        horaEntrada=values["-RESERVA-HORA-ENTRADA-"]
        minutosEntrada=values["-RESERVA-MINUTO-ENTRADA-"]
        tempoEntrada= f"{horaEntrada}:{minutosEntrada}:00"
        formato="%d-%m-%Y %H:%M:%S"
        resultado=False
        if dataEntrada and dataEntrada!="":
            periodoEntradaStr=f"{dataEntrada} {tempoEntrada}"
            print(f"Periodo: {periodoEntradaStr}")
            periodoEntradaDateTime=datetime.strptime(periodoEntradaStr,formato)
       
            print(periodoEntradaDateTime)
            
            dataSaida=values["-DT-SAIDA-"]
            horaSaida=values["-RESERVA-HORA-SAIDA-"]
            minutosSaida=values["-RESERVA-MINUTO-SAIDA-"]
            tempoSaida= f"{horaSaida}:{minutosSaida}:00"
            
            if dataSaida and dataSaida!="":
                periodoSaidaStr=f"{dataSaida} {tempoSaida}"
                periodoSaidaDateTime=datetime.strptime(periodoSaidaStr,formato)
                
                if periodoEntradaDateTime == periodoSaidaDateTime:
                    sg.popup_error('Erro', 'O periodo de entrada nao pode ser o mesmo que o periodo de saida!')
                    resultado= False
                elif periodoEntradaDateTime > periodoSaidaDateTime:                    
                    sg.popup_error('Erro', 'O periodo de entrada nao pode ser maior que o periodo de saida!')
                    resultado= False
                else:
                    self.dataTempoEntrada=periodoEntradaDateTime
                    self.dataTempoSaida=periodoSaidaDateTime
                    resultado= True

            else:
                sg.popup_error('Erro', 'Voce selecionou uma data de Saida invalida!')
            
        else:
            sg.popup_error('Erro', 'Voce selecionou uma data de entrada invalida!')
            
        return resultado
        
 
    def calcularPrecoPagar(self,dataTempoEntrada,dataTempoSaida, precoHoraParque):
        diferenca=dataTempoSaida-dataTempoEntrada
        totalHoras=diferenca.total_seconds()/3600
        precoPagar=totalHoras*precoHoraParque
        return precoPagar
    
    
    def reservarVaga(self,window,values):
       # self.servico_reserva. 
        id_vaga=self.validarVagaSelecionada(values)
        id_usuario=self.usuario_logado.id_usuario
        id_viatura=self.validarMatriculaSelecionada(values)
        self.dataTempoEntrada=None
        self.dataTempoSaida=None
        if id_vaga>0 and id_usuario>0 and id_viatura >0 and self.validarPeriodoEscolhido(values):
            precoPagar=self.calcularPrecoPagar(self.dataTempoEntrada,self.dataTempoSaida,self.tela_reserva_vaga.parque_selecionado.preco)
            print(f"Saldo actual {self.saldoActual}")
            print(f"Tens que pagar {precoPagar}")
            if self.saldoActual >=precoPagar:

                resposta = sg.popup_yes_no(f"Confirma o pagamento de {precoPagar}mts para a reserva da vaga?", title="Confirmar")
                if resposta == "Yes":
                    print("Confirmado")
                    dataEntrada= values["-DT-ENTRADA-"]    
                    horaEntrada=values["-RESERVA-HORA-ENTRADA-"]
                    minutosEntrada=values["-RESERVA-MINUTO-ENTRADA-"]
                    tempoEntrada= f"{horaEntrada}:{minutosEntrada}:00"
                    #print(f"Preco a pagar: {precoPagar}")
                    
                    dataSaida=values["-DT-SAIDA-"]
                    horaSaida=values["-RESERVA-HORA-SAIDA-"]
                    minutosSaida=values["-RESERVA-MINUTO-SAIDA-"]
                    tempoSaida= f"{horaSaida}:{minutosSaida}:00"
                    reservaDTO =ParqueamentoApp.ReservaDTO(-1,dataEntrada,tempoEntrada,dataSaida,tempoSaida,precoPagar,id_vaga,id_usuario,id_viatura)
                    sucesso=self.servico_reserva.criarReserva(reservaDTO)       
                    
                    if sucesso:
                        #Mudar o estado da vaga para ocupado: 1
                        self.servico_vaga.actualizarEstadoVaga(id_vaga, 1)                  
                        self.tela_reserva_vaga.vagas_disponiveis=self.listarVagasDisponiveis(self.tela_reserva_vaga.parque_selecionado.id_parque)
                        
                        #Debitar o valor
                        self.debitar(self.tela_usuario_comum.window,precoPagar)
                        
                        window["-COMBO-VAGA-"].update(values=self.tela_reserva_vaga.vagas_disponiveis,value=self.tela_reserva_vaga.vagas_disponiveis[0] if self.tela_reserva_vaga.vagas_disponiveis else '')
                        window["-DT-ENTRADA-"].update( '')
                        window["-DT-SAIDA-"].update( '')
                        
                        
                        #window["-COMBO-MATRICULA-"].update(values=self.listarMatriculaViaturas(),default_value=self.[0] if self. else '')
                        

                        sg.popup("Voce Efectuou a reserva com sucesso", title="Sucesso")
                    else:
                        sg.popup_error('Erro', 'Falha ao ao reservar a vaga.')    

            else:
                 sg.popup_error('Erro', f'Voce nao tem saldo suficiente na tua conta para poder reservar a vaga!\nA reserva custa {precoPagar}mts e voce so tem {self.saldoActual}mts\nPor favor recarregue a sua conta')    

    
    def listarReservasVaga(self):
        """Lista as reservas de vagas que o usuario ja efectuou."""
        self.listaReservasVagaDTO=self.servico_reserva.listarReservas(self.usuario_logado.id_usuario)
        listaReservaVagas=[]
        if self.listaReservasVagaDTO:
            for reservaDTO in self.listaReservasVagaDTO:
                #print("-------------")
               # numeroVaga=self.buscarNumeroVagaReservada(reservaDTO.id_vaga)
                #print(f"Vaga: {numeroVaga}")
                matriculaViatura=self.buscarMatriculaViaturaReservada(reservaDTO.id_viatura)
         #      print(f"Matricula: {matriculaViatura}")
                listaReservaVagas.append([reservaDTO.id_reserva,reservaDTO.data_entrada,reservaDTO.hora_entrada,reservaDTO.data_saida,reservaDTO.hora_saida,reservaDTO.preco_total,reservaDTO.id_vaga,matriculaViatura])
            
        #print(f"lista: {listaReservaVagas}")
        
        return listaReservaVagas              
            
       
#Funcoes exclusivas do administrador
    def colocarDadosParque(self,window,parqueDTO):
        window["-PARQUE_NOME-"].update(parqueDTO.nome)
        window["-COMBO-PROVINCIA-"].update(parqueDTO.provincia)
        window["-PARQUE_LOCALIZACAO-"].update(parqueDTO.localizacao)
        window["-PARQUE_TEL-"].update(parqueDTO.telefone)
        window["-PARQUE_HORARIO-"].update(parqueDTO.horario)
        window["-COMBO-COBERTURA-"].update(parqueDTO.cobertura)
        window["-PARQUE_PRECO-"].update(parqueDTO.preco)
        window["-BTN_ADICIONAR_PARQUE-"].update(disabled=True)
        window["-BTN_ATUALIZAR_PARQUE-"].update(disabled=False)
        window["-BTN_REMOVER_PARQUE-"].update(disabled=False)
        
        
        
    def adicionarParque(self,window,values):
        nome=values["-PARQUE_NOME-"]
        provincia=values["-COMBO-PROVINCIA-"]
        localizacao=values["-PARQUE_LOCALIZACAO-"]
        telefone=values["-PARQUE_TEL-"]
        horario=values["-PARQUE_HORARIO-"]
        cobertura=values["-COMBO-COBERTURA-"]
        preco=values["-PARQUE_PRECO-"]
        url=""
        
        if validarNome(nome) and len(provincia)>3 and validarTelefone(telefone) and len(horario)>=2 and cobertura in ["COBERTO", "NAO_COBERTO"] and validar_dinheiro_string(preco):
            parqueDTO=ParqueamentoApp.ParqueDTO(-1,nome,provincia,localizacao,telefone,horario,cobertura,validar_dinheiro(preco),url)
            idParque=self.servico_parque.adicionarParque(parqueDTO)
            if idParque>0: 
                window["-TABELA_PARQUES-"].update(values=self.listarParques())
                
                #Criar vagas para o parque
                numeroVagas=50
                self.servico_vaga.adicionarVaga(idParque,numeroVagas)
                
                sg.popup("Sucesso","O parque foi adicionado com sucesso")
            else:
                sg.popup_error("Erro","Houve uma falha ao adicionar o novo parque.")
     
    def removerParque(self,window,parqueDTO):
        if parqueDTO.id_parque >0:
            resposta=sg.popup_yes_no(f"Voce tem certeza que quer remover o parque '{parqueDTO.nome}' ?")
            if resposta =="Yes":
                resultado=self.servico_parque.removerParque(parqueDTO.id_parque)
                if resultado:
                    window["-TABELA_PARQUES-"].update(values=self.listarParques())
                    sg.popup("Sucesso", "Você removeu o parque com sucesso")
        
        
    def limparDadosParque(self,window):
        """Limpa os dados do parque selecionadao"""
        window["-PARQUE_NOME-"].update("")
        window["-COMBO-PROVINCIA-"].update(value="")
        window["-PARQUE_LOCALIZACAO-"].update("")
        window["-PARQUE_TEL-"].update("")
        window["-PARQUE_HORARIO-"].update("")
        window["-COMBO-COBERTURA-"].update(value="")
        window["-PARQUE_PRECO-"].update("")
        window["-BTN_ADICIONAR_PARQUE-"].update(disabled=False)
        window["-BTN_ATUALIZAR_PARQUE-"].update(disabled=True)
        window["-BTN_REMOVER_PARQUE-"].update(disabled=True)
        

       


    def executar(self):
        while True:
            # Captura eventos de TODAS as janelas abertas
            window, event, values = sg.read_all_windows()
            

            # --- EVENTOS DA TELA DE LOGIN ---
            if self.tela_login !=None  and window == self.tela_login.window:
                if event ==sg.WIN_CLOSED:
                    break
                
                elif event == "-BTN-LOGIN-":
                    telefone = values["-LOGIN-TEL-"].strip()
                    senha = values["-LOGIN-SENHA-"].strip()

                    if validarTelefone(telefone) and validarSenha(senha):  # Validação simples

                        try:
                            # Chamada CORBA ao serviço de autenticação
                            user_dto = self.servico_usuario.login(telefone, senha)
    
                            if user_dto and user_dto.id_usuario > 0:
                                sg.popup("Login efetuado com sucesso!", title="Sucesso")
                                self.usuario_logado = user_dto
                                print(user_dto.nome)
                                self.tela_login.ocultar()
                                
                                if self.usuario_logado.tipo==0: #Mostra a tela do usuario comum
                                    #self.tela_usuario_comum.usuario_logado=user_dto
                                    
                                    #Verificar se ele ja possui uma conta bancaria
                                    self.verificarContaBancaria()
                                    self.saldoActual =self.servico_conta.consultarSaldo(self.usuario_logado.id_usuario)
                                    
                                    #Pesquisar os dados que o usuario vai precisar usando as funcoes listarParques, listarViaturas, listarTransacoes.
                                    self.tela_usuario_comum= TelaUsuarioComum(user_dto,self.listarParques(),self.listarViaturas(),self.listarTransacoes(),self.listarReservasVaga(),self.saldoActual)
                                    self.tela_usuario_comum.minhas_reservas=self.listarReservasVaga()
                                    #listaParques=None
     
                                    
                                else:
                                    # Mostra a tela de admin
                                    self.tela_administrador=TelaAdministrador(user_dto,self.listarParques())
                                
                            else:
                                sg.popup_error("Telefone ou senha incorretos.")
                        except Exception as e:
                            sg.popup_error(f"Erro de comunicação CORBA: {e}")
                        
                    else:
                        sg.popup_error('Por favor, preencha usuário e senha correctamente.')
                elif event == "-BTN-TELA-CADASTRO-":
                    print("Cadastrar")
                    self.tela_login.ocultar()
                    self.tela_cadastro = TelaCadastroUsuario()
                
            #--- Eventos da tela de cadastro ---
            elif self.tela_cadastro!=None and window == self.tela_cadastro.window:
                if event ==sg.WIN_CLOSED:
                    break
                elif event == "-BTN-CAD-USER-":

                    nome = values["-CAD-NOME-"].strip()
                    telefone = values["-CAD-TEL-"].strip()
                    senha = values["-CAD-SENHA-"].strip()

                    if validarNome(nome) and validarTelefone(telefone) and validarSenha(senha):
                        # Tipo 0 = Cliente normal
                        novo_user = ParqueamentoApp.UsuarioDTO(
                            -1, nome, telefone, senha, 0)
                        
                        try:
                            self.servico_usuario.cadastrar(novo_user)
                            
                            sg.popup("Cadastro efetuado! Já pode realizar o login.")
                            self.tela_login.exibir()

                        except Exception as e:
                            sg.popup_error(f"Erro ao cadastrar: {e}")
                    else:
                        sg.popup("Preencha todos os campos do cadastro.")
          
            
            #---Eventos da tela do usuario comum ---
            elif self.tela_usuario_comum !=None  and window==self.tela_usuario_comum.window:     
                # Fechar aplicação
                if event == sg.WIN_CLOSED:
                    break

                # 1. EVENTOS DA TAB PARQUES (Seleção na Tabela para Reserva)
                if event == '-TABELA_PARQUES-':
                    
                    linhas_selecionadas = values['-TABELA_PARQUES-']
                    if linhas_selecionadas:
                        indice = linhas_selecionadas[0]
                        parqueDTO=self.listaParquesDTO[indice]
                       # print(f"Parque selecionado {parqueDTO}")
                   
            
                        
                        #sg.popup_error('Erro', ' reservar.')
                        if not self.listaViaturasDTO:
                            sg.popup_error('Erro', 'Você precisa cadastrar pelo menos uma viatura antes de reservar.')
                            #Abrir a tab para dicionar viaturas
                        else:
                            self.tela_usuario_comum.ocultar()
                            self.tela_reserva_vaga= TelaReservaVaga(self.listarMatriculaViaturas(),parqueDTO,self.listarVagasDisponiveis(parqueDTO.id_parque))  
                    
                # EVENTOS DA TABELA PERFIL
                if event == "-BTN_DEPOSITAR-":
                    self.depositar(self.tela_usuario_comum.window,values)
                if event == "-BTN_ATUALIZAR_PERFIL-":
                    self.actualizarDadosUsuario(self.tela_usuario_comum.window,values)
                
                #EVENTO QUANDO UMA MARCA E SELECIONADA
                if event == "-MARCA-":
                    self.selecionarModelosCarro(self.tela_usuario_comum.window,values)
                        
               # EVENTOS DA TABELA Minhas Viaturas
                if event == "-BTN_ADD_VIATURA-":
                   self.adicionarViatura(self.tela_usuario_comum.window,values)
                   
            #---Eventos da tela de Reserva de vaga ---
            elif self.tela_reserva_vaga !=None  and window==self.tela_reserva_vaga.window:   
                # EVENTO DE CANCELAR A RESERVA
                if event == "-CANCELAR_RESERVA-" or event==sg.WIN_CLOSED:
                    self.tela_reserva_vaga.fechar()
                    self.tela_usuario_comum.exibir()
                
                if event == "-BTN-DATA-ENTRADA-":
                    self.escolherData("Selecione a Data de Entrada",self.tela_reserva_vaga.window,"-DT-ENTRADA-")
                
                if event == "-BTN-DATA-SAIDA-":
                    self.escolherData("Selecione a Data de Saida",self.tela_reserva_vaga.window,"-DT-SAIDA-")
                
                if event == "-BTN_CONFIRMAR_RESERVA-":
                    self.reservarVaga(self.tela_reserva_vaga.window,values)
            
            
             #---Eventos da tela de administrador---
            elif self.tela_administrador !=None  and window==self.tela_administrador.window:  
                
                if event ==sg.WIN_CLOSED:
                    break
                
               # . EVENTOS DA TAB PARQUES (Seleção na Tabela para Edicao)
                if event == '-TABELA_PARQUES-':
                    
                    linhas_selecionadas = values['-TABELA_PARQUES-']
                    if linhas_selecionadas:
                        indice = linhas_selecionadas[0]
                        parqueDTO=self.listaParquesDTO[indice]
                        
                        self.colocarDadosParque(self.tela_administrador.window,parqueDTO)

                
                # EVENTO PARA ADICIONAR PARQUE
                if event == '-BTN_ADICIONAR_PARQUE-':
                    self.adicionarParque(self.tela_administrador.window,values)
                    self.limparDadosParque(self.tela_administrador.window)
                
                
                # EVENTO PARA ACTUALIZAR PARQUE
                if event == '-BTN_ATUALIZAR_PARQUE-':
                    pass
                    #Voltar a habilitar o botao adicionar
                    
                if event == "-BTN_REMOVER_PARQUE-":
                    self.removerParque(self.tela_administrador.window,parqueDTO)
                    self.limparDadosParque(self.tela_administrador.window)
                    
                # EVENTO PARA Limpar os dados selecionados
                if event == '-BTN_LIMPAR-':
                    self.limparDadosParque(self.tela_administrador.window)
                


                    

if __name__ == '__main__':
    app = GerenciadorJanelas()
    app.executar()
    
    