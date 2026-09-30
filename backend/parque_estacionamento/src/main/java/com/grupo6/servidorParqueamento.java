package com.grupo6;

/**
 * Para Compilar arquivos normalmente use o comando: javac *.java CalculadoraApp/*.java
 * Executar o daemon do serviço(Servidor) de nomes "java orbd -ORBInitialPort 1050"
 * Rodar o servidor "java servidorParqueamento -ORBInitialPort 1050 -ORBInitialHost localhost"
**/

//package com.grupo6.ParqueamentoApp;

//Importacao dos arquivos
import com.grupo6.ParqueamentoApp.Parque;
import com.grupo6.ParqueamentoApp.ParqueHelper;

import com.grupo6.ParqueamentoApp.Reserva;
import com.grupo6.ParqueamentoApp.ReservaHelper;

import com.grupo6.ParqueamentoApp.Usuario;
import com.grupo6.ParqueamentoApp.UsuarioHelper;

import com.grupo6.ParqueamentoApp.Vaga;
import com.grupo6.ParqueamentoApp.VagaHelper;

import com.grupo6.ParqueamentoApp.Viatura;
import com.grupo6.ParqueamentoApp.ViaturaHelper;

import java.util.Properties;

import org.omg.CORBA.ORB;
import org.omg.CosNaming.NameComponent;
import org.omg.CosNaming.NamingContextExt;
import org.omg.CosNaming.NamingContextExtHelper;

import org.omg.PortableServer.POA;
import org.omg.PortableServer.POAHelper;

/**
 * Primeiro temos que rodar o servidor de nomes
 * O servidorCORBA roda e regista o objecto no servidor de nome
 * O cliente faz acesso ao servidor de nomes para poder acessar a referência do objecto
 * 
 * 
 * servidorCORBA
 */
public class servidorParqueamento {

    public servidorParqueamento(){}
    public servidorParqueamento(String Host,String Port){}

    public static void main(String[] args) {
        try{
            //Criar e inicializa o ORB
           // ORB orb = ORB.init(args,null);
           String Host="localhost";
           String Port ="1050";

            //Propreidades
            Properties props= new Properties();
            // Define o IP ou Hostname do servidor CORBA
            props.put("org.omg.CORBA.ORBInitialHost", Host); 
            // Define a porta (geralmente obrigatório em conjunto com o host)
            props.put("org.omg.CORBA.ORBInitialPort", Port); 

            //Criar e inicializa o ORB
            ORB orb = ORB.init(args,props);


            //Obter o  RootPOA (Portable Object Adapter) e ativa o gerenciador POA
            POA rootpoa =POAHelper.narrow(orb.resolve_initial_references("RootPOA"));
            rootpoa.the_POAManager().activate(); 

            //Criar os serviços (Implementacao deles) e registra ele com o ORB (Object Request Broker)
            ParqueImpl parqueImpl = new ParqueImpl();

            ReservaImpl reservaImpl = new ReservaImpl();

            UsuarioImpl usuarioImpl = new UsuarioImpl();

            VagaImpl vagaImpl = new VagaImpl();

            ViaturaImpl viaturaImpl = new ViaturaImpl();

            //Registar os Objectos (Calculadora) no POA:  Obtém a referência ao serviço disponibilizado pelo servidor 
            org.omg.CORBA.Object parqueRef = rootpoa.servant_to_reference(parqueImpl);
            org.omg.CORBA.Object reservaRef = rootpoa.servant_to_reference(reservaImpl);
            org.omg.CORBA.Object usuarioRef = rootpoa.servant_to_reference(usuarioImpl);
            org.omg.CORBA.Object vagaRef = rootpoa.servant_to_reference(vagaImpl);
            org.omg.CORBA.Object viaturaRef = rootpoa.servant_to_reference(viaturaImpl);

            
            //Converter para a referencia Calculadora (Fazer narrow)
            Parque parque = ParqueHelper.narrow(parqueRef);
            Reserva reserva = ReservaHelper.narrow(reservaRef);
            Usuario usuario = UsuarioHelper.narrow(usuarioRef);
            Vaga vaga = VagaHelper.narrow(vagaRef);
            Viatura viatura = ViaturaHelper.narrow(viaturaRef);


            //Obter a referência para o serviço de nomes(Servidor de nomes/ Naming Service)
            org.omg.CORBA.Object objRef= orb.resolve_initial_references("NameService");
            NamingContextExt namingRef = NamingContextExtHelper.narrow(objRef);

            //Criar nome para o objecto: Vincula a referência do objecto a um nome, no servidor de nomes

            //Registar Parque
            NameComponent parqueName[] = namingRef.to_name("Parque");

            //Registar o Naming Service
            namingRef.rebind(parqueName,parque);


            //Registar Reserva
            NameComponent reservaName[] = namingRef.to_name("Reserva");
            namingRef.rebind(reservaName,reserva);

            //Registar Usuario
            NameComponent usuarioName[] = namingRef.to_name("Usuario");
            namingRef.rebind(usuarioName,usuario);

            //Registar Vaga
            NameComponent vagaName[] = namingRef.to_name("Vaga");
            namingRef.rebind(vagaName,vaga);

            //Registar Viatura
            NameComponent viaturaName[] = namingRef.to_name("Viatura");
            namingRef.rebind(viaturaName,viatura);



            System.out.println("Servidor pronto e aguardando pedidos!" +"\nIP: "+Host+"\nPorta: "+Port);

            //Aguarda pela invocação dos clientes
            orb.run();
            
        } catch (Exception e){
            System.err.println("Erro: "+e);
            e.printStackTrace(System.out);

        }



    }
}
