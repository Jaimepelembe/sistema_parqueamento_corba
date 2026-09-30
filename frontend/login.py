import sys
from omniORB import CORBA


# 1. Importe o módulo/interface gerado pelo omniidl
# Exemplo: supondo que a sua interface IDL esteja no namespace "grupo6" e se chame "UsuarioService"
import ParqueamentoApp
import CosNaming

def main():
    """"
    # 2. Inicializa o ORB
    orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

    # 3. Cole aqui a string IOR gerada pelo servidor Java/CORBA
    ior = "IOR:000000000000002b49444c3a6f6d672e6f72672f436f734e616d696e672f4e616d696e67436f6e746578744578743a312e30000000000001000000000000009e00010200000000103136392e3235342e3138392e31303200041a000000000045afabcb0000000020000f424000000001000000000000000200000008526f6f74504f41000000000d544e616d65536572766963650000000000000008000000010000000114000000000000020000000100000020000000000001000100000002050100010001002000010109000000010001010000000026000000020002" 
""" 
    try:
        
        # Monta o argumento no formato padrão CORBA
        # Exemplo resultante: -ORBInitRef NameService=corbaloc:iiop:192.168.1.50:1050/NameService
        initial_host="localhost"
        initial_port=1050
        init_ref_arg = f"NameService=corbaname:iiop:{initial_host}:{initial_port}/NameService"

        # Adiciona aos argumentos do sistema que serão lidos pelo ORB
        orb_args = sys.argv + ["-ORBInitRef", init_ref_arg]
        orb = CORBA.ORB_init(orb_args)
        
        naming_service = orb.resolve_initial_references("NameService")
        root_context = naming_service._narrow(CosNaming.NamingContext)
   
        name = [CosNaming.NameComponent("Usuario", "")]
        obj = root_context.resolve(name)

        # 5. Faz o "narrow" para converter o objeto no tipo específico da sua Interface IDL
        usuario_service = obj._narrow(ParqueamentoApp.Usuario)

        if usuario_service is None:
            print("Erro: O objeto remoto não é do tipo UsuarioService")
            sys.exit(1)
        
        resultado =usuario_service.login("829876543", "senha123")
            
    except CORBA.Exception as ex:
        print(f"Erro na comunicação CORBA: {ex}")        


"""
        name = [CosNaming.NameComponent("Parque", "")]
        obj = root_context.resolve(name)

        # 5. Faz o "narrow" para converter o objeto no tipo específico da sua Interface IDL
        parque_service = obj._narrow(ParqueamentoApp.Parque)

        if parque_service is None:
            print("Erro: O objeto remoto não é do tipo parqueService")
            sys.exit(1)

        print("Conexão estabelecida com sucesso via IOR!")



        # 6. Aceder às funções do utilizador (métodos definidos na IDL)
        
        # Exemplo A: Autenticar / Login
        resultado_login = parque_service.pesquisarPorCategoria("preco")
        for parque in resultado_login:
            print(parque.preco)
            print(parque.localizacao)
            
    """
        
  

""""
        # Exemplo B: Buscar dados do utilizador
        dados_usuario = usuario_service.obterUsuarioPorId(1)
        print(f"Nome do Utilizador: {dados_usuario.nome}")
        print(f"Email do Utilizador: {dados_usuario.email}")

        # Exemplo C: Cadastrar novo utilizador
        sucesso = usuario_service.cadastrarUsuario("Jaime", "jaime@email.com", "senha123")""
        if sucesso:
            print("Utilizador cadastrado com sucesso!")
"""


if __name__ == "__main__":
    main()

