package com.grupo6;

/**
 * Para Compilar arquivos normalmente use o comando: javac *.java PagamentoApp/*.java
 * Executar o daemon do serviço(Servidor) de nomes "java orbd -ORBInitialPort 1050"
 * Rodar o servidor "java servidorPagamento -ORBInitialPort 1050 -ORBInitialHost localhost"
**/

//package com.grupo6.PagamentoApp;

//Importacao dos arquivos
import com.grupo6.PagamentoApp.Conta;
import com.grupo6.PagamentoApp.ContaHelper;

import com.grupo6.PagamentoApp.Transacao;
import com.grupo6.PagamentoApp.TransacaoHelper;

import java.util.Properties;

import org.omg.CORBA.ORB;
import org.omg.CosNaming.NameComponent;
import org.omg.CosNaming.NamingContextExt;
import org.omg.CosNaming.NamingContextExtHelper;

import org.omg.PortableServer.POA;
import org.omg.PortableServer.POAHelper;

/**
 * Primeiro temos que rodar o servidor de nomes
 * O servidorPagamento roda e regista o objecto no servidor de nome
 * O cliente faz acesso ao servidor de nomes para poder acessar a referência do objecto
 * 
 * 
 * 
 */
public class servidorPagamento {

    public servidorPagamento(){}
    public servidorPagamento(String Host,String Port){}

    public static void main(String[] args) {
        try{
            //Criar e inicializa o ORB
           // ORB orb = ORB.init(args,null);
           String Host="localhost";
           String Port ="1050";

            //Propriedades
            Properties props= new Properties();
            // Define o IP ou Hostname do servidor CORBA
            props.put("org.omg.CORBA.ORBInitialHost", Host); 
            // Define a porta (geralmente obrigatório em conjunto com o host)
            props.put("org.omg.CORBA.ORBInitialPort", Port); 

            //Cria e inicializa o ORB
            ORB orb = ORB.init(args,props);


            //Obter o  RootPOA (Portable Object Adapter) e ativa o gerenciador POA
            POA rootpoa =POAHelper.narrow(orb.resolve_initial_references("RootPOA"));
            rootpoa.the_POAManager().activate(); 

            //Criar os serviços (Implementacao deles) e registra ele com o ORB (Object Request Broker)
            ContaImpl contaImpl = new ContaImpl();
            TransacaoImpl transacaoImpl = new TransacaoImpl();


            //Registar os Objectos (contaImpl e transacaoImpl) no POA:  Obtém a referência ao serviço disponibilizado pelo servidor 
            org.omg.CORBA.Object contaRef = rootpoa.servant_to_reference(contaImpl);
            org.omg.CORBA.Object transacaoRef = rootpoa.servant_to_reference(transacaoImpl);

            
            //Converter para a referencia Conta e Transacao (Fazer narrow)
            Conta conta = ContaHelper.narrow(contaRef);
            Transacao transacao = TransacaoHelper.narrow(transacaoRef);

            //Obter a referência para o serviço de nomes(Servidor de nomes/ Naming Service)
            org.omg.CORBA.Object objRef= orb.resolve_initial_references("NameService");
            NamingContextExt namingRef = NamingContextExtHelper.narrow(objRef);

            //Criar nome para o objecto: Vincula a referência do objecto a um nome, no servidor de nomes

            //Registar Conta
            NameComponent contaName[] = namingRef.to_name("Conta");

            //Registar o Naming Service
            namingRef.rebind(contaName,conta);

            //Registar Transacao
            NameComponent transacaoName[] = namingRef.to_name("Tansacao");
            namingRef.rebind(transacaoName,transacao);



            System.out.println("Servidor de pagamento pronto e aguardando pedidos!" +"\nIP: "+Host+"\nPorta: "+Port);

            //Aguarda pela invocação dos clientes
            orb.run();
            
        } catch (Exception e){
            System.err.println("Erro: "+e);
            e.printStackTrace(System.out);

        }



    }
}
