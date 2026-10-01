import PySimpleGUI as sg
from telas.login import TelaLogin
from telas.TelaPrincipal import TelaPrincipal
from telas.cadastraUsuario import TelaCadastroUsuario
from telas.telaUsuarioComum import TelaUsuarioComum
from telas.telaReservaVaga import TelaReservaVaga

from validacoes import validarSenha
from validacoes import validarTelefone
from validacoes import validarNome

#Importacoes de corba
import sys
from omniORB import CORBA
import CosNaming

# Importar o módulo gerado pelo omniidl a partir do IDL
import ParqueamentoApp






class GerenciadorJanelas:
    """Classe controladora que gerencia a transição entre telas e eventos."""
    def __init__(self):
        self.tela_login = TelaLogin()
        self.tela_usuario_comum = None
        self.tela_cadastro = None#TelaCadastroUsuario()
        self.tela_reserva_vaga=None
        self.inicializarCORBA()
        self.listaParquesDTO=None
        self.listaViaturasDTO=None
        self.listaTransacoesDTO=None

        

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

        # Guarda o utilizador autenticado após o login
        self.usuario_logado = None
    
    
    
    def obter_servico(self, nome_servico, interface_class):
        name = [CosNaming.NameComponent(nome_servico, "")]
        obj = self.root_context.resolve(name)
        return obj._narrow(interface_class)
        
        
    
    
    def encerrar_aplicacao(self):
        if self.tela_login:
            self.tela_login.fechar()
        if self.tela_principal:
            self.tela_principal.fechar()
        if self.tela_cadastro:
            self.tela_cadastro.fechar()
   
   
   
    def executar(self):
        while True:
            # Captura eventos de TODAS as janelas abertas
            window, event, values = sg.read_all_windows()
            

            # --- EVENTOS DA TELA DE LOGIN ---
            if window == self.tela_login.window:
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
                                
                                if self.usuario_logado.tipo==0:
                                    #self.tela_usuario_comum.usuario_logado=user_dto
                                    #Pesquisar os dados que o usuario vai precisar
                                    #Viaturas
                                    self.listaViaturasDTO=self.servico_viatura.listarViaturas(self.usuario_logado.id_usuario)
                                    print(self.listaViaturasDTO)
                                    print("Buscou viaturas")
                                    listaViaturas=[]
                                    for viaturaDTO in self.listaViaturasDTO:
                                        listaViaturas.append([viaturaDTO.marca,viaturaDTO.modelo,viaturaDTO.matricula])
                                        print(viaturaDTO.matricula)
                                    
                                    
                                    self.listaParquesDTO=self.servico_parque.pesquisarPorCategoria("nome")
                                    listaParques=[]
                                    for parqueDTO in self.listaParquesDTO:
                                        listaParques.append([parqueDTO.nome,parqueDTO.provincia,parqueDTO.localizacao,parqueDTO.telefone,parqueDTO.horario,parqueDTO.cobertura,parqueDTO.preco])
                                        print(parqueDTO.nome)
                                    
                                    print("Tela de login")
                                    #print(listaParques)
                                    self.tela_usuario_comum= TelaUsuarioComum(user_dto,listaParques,listaViaturas,[])
                                    listaParques=None
                                    #listaViaturas=None
                                  
                                    
                                    pass # Mostra a tela normal
                                else:
                                    pass # Mostra a tela de admin
                                
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
                
            
            #---Eventos da tela do usuario comum ---
            elif window ==self.tela_usuario_comum.window:     
                # Fechar aplicação
                if event ==sg.WIN_CLOSED:
                    break

                # 1. EVENTOS DA TAB PARQUES (Seleção na Tabela para Reserva)
                if event == '-TABELA_PARQUES-':
                    #Listar as viaturas
                    
                    
                    linhas_selecionadas = values['-TABELA_PARQUES-']
                    if linhas_selecionadas:
                        indice = linhas_selecionadas[0]
                       # parque_selecionado = self.lista_parques[indice]
                        parqueDTO=self.listaParquesDTO[indice]
                        print(f"Parque selecionado {parqueDTO}")
                        #nome_parque = parque_selecionado[0]
                        #preco_parque = parque_selecionado[6]
                        print("entrou na reserva")
                        #minhas_viaturas, parqueSelecioinado,vagasDisponiveis
                        listaViaturas=[]
                        for viaturaDTO in self.listaViaturasDTO:
                            listaViaturas.append([viaturaDTO.marca,viaturaDTO.modelo,viaturaDTO.matricula])
                            print(viaturaDTO.matricula)
                        
                        self.tela_reserva_vaga= TelaReservaVaga(listaViaturas,parqueDTO,[])  
                        
                        #sg.popup_error('Erro', ' reservar.')
                        if not self.listaViaturasDTO:
                            sg.popup_error('Erro', 'Você precisa cadastrar pelo menos uma viatura antes de reservar.')
                            #Abrir a tab para dicionar viaturas
                        else:
                            self.tela_usuario_comum.ocultar()
                            self.tela_reserva_vaga= TelaReservaVaga()  
                    
            #---Eventos da tela de cadastro ---
            elif window == self.tela_cadastro.window:
                if event ==sg.WIN_CLOSED:
                    break
                elif event == "-BTN-CAD-USER-":
                    print("Cadastrar")
                        
                    nome = values["-CAD-NOME-"].strip()
                    telefone = values["-CAD-TEL-"].strip()
                    senha = values["-CAD-SENHA-"].strip()

                    if validarNome(nome) and validarTelefone(telefone) and validarSenha(senha):
                        # Tipo 0 = Cliente normal
                        print("Validados")
                        novo_user = ParqueamentoApp.UsuarioDTO(
                            -1, nome, telefone, senha, 0)

                        print(f"Novo: {novo_user.id_usuario}")
                        
                        try:
                            self.servico_usuario.cadastrar(novo_user)
                            sg.popup("Cadastro efetuado! Já pode realizar o login.")
                            self.tela_login.exibir()

                        except Exception as e:
                            sg.popup_error(f"Erro ao cadastrar: {e}")
                    else:
                        sg.popup("Preencha todos os campos do cadastro.")
        
            
                

            

if __name__ == '__main__':
    app = GerenciadorJanelas()
    app.executar()