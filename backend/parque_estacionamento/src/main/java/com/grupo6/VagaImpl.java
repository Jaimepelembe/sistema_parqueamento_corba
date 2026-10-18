package com.grupo6;

import com.grupo6.ParqueamentoApp.VagaPOA;

import java.util.Map;

import com.grupo6.ParqueamentoApp.Observador;
import com.grupo6.ParqueamentoApp.UsuarioDTO;
import com.grupo6.ParqueamentoApp.VagaDTO;
import com.grupo6.dao.VagaDAO;

import com.grupo6.ParqueamentoApp.Observador;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class VagaImpl extends VagaPOA {
    private final Object lock = new Object();
    private final Map<Integer, Observador> observadores = new HashMap<Integer, Observador>();
    private int proximoId = 1;
    private VagaDAO vagaDAO;


    public VagaImpl() {

        
    }


    @Override
    public void adicionarVaga(int id_parque, int numero_de_vagas){
        synchronized (lock){
        vagaDAO= new VagaDAO();
        VagaDTO vaga= null;

        for ( int i=0; i<numero_de_vagas;i++){
           String numero="A-"+(i+1);
           //System.out.println(numero);
            vaga = new VagaDTO(-1,numero, 0, id_parque);
            vagaDAO.adicionarVaga(vaga);
        }
        //VagaDTO[] vagas=null;
        //vagas=listarVagasDisponiveis(id_parque);
        //notificarTodos(vagas);

    }
    }

    @Override
    public boolean actualizarEstadoVaga(int id_vaga, int estadoVaga){
        synchronized (lock){
        vagaDAO= new VagaDAO();
        boolean resultado=false;
        resultado=vagaDAO.actualizarEstadoVaga(id_vaga, estadoVaga);

        return resultado;
    }          
    }

    @Override
    public boolean actualizarEstadoVagaNotificacao(int id_vaga, int estadoVaga){
        synchronized (lock){
        vagaDAO= new VagaDAO();
        boolean resultado=false;
        resultado=vagaDAO.actualizarEstadoVaga(id_vaga, estadoVaga);
        if (resultado){ //Buscar a nova lista de actualizada e enviar para todos os usuarios comum
            int id_parque=vagaDAO.buscarIdParque(id_vaga);
            //System.out.println("Id do parque: "+id_parque);

            if (id_parque >0){
                VagaDTO[] vagas=null;
                vagas=listarVagasDisponiveis(id_parque);
                notificarTodos(vagas);
            }
        }
  
        return resultado;
    }          
    }



    /**
    private int buscarIdParque(int id_vaga){
        synchronized (lock){

            vagadao= new VagaDAO();
        }

    }* */

    @Override
    public VagaDTO[] listarVagas(int id_parque) {
        vagaDAO = new VagaDAO();
        VagaDTO[] listaVagas=   vagaDAO.listarVagas(id_parque);

        return listaVagas;}


@Override 
public VagaDTO[] listarVagasDisponiveis(int id_parque) {
    synchronized (lock){
    vagaDAO = new VagaDAO();
    VagaDTO[] listaVagas=   vagaDAO.listarVagasDisponivies(id_parque);

    return listaVagas;}
}


    
    @Override 
    public int numeroTotalVagas(int id_parque) {
        int numeroTotal=0;
        vagaDAO = new VagaDAO();
        numeroTotal= vagaDAO.numeroTotalVagas(id_parque);

        return numeroTotal;}


    @Override
    public int registarObservador(Observador obs){
        int id;
        int total;
        synchronized (lock){
            id=proximoId++;
            observadores.put(id,obs);
            total=observadores.size();
        }

        System.out.println("Observador "+id +"registado (" +total+" no total)");
        return id;
    }

    @Override 
    public void removerObservador(int id){
        synchronized (lock){
            observadores.remove(id);
        }
       System.out.println("Observador "+id + " removido");
    }


    private void notificarTodos(VagaDTO[] vagas) {
    Iterator<Map.Entry<Integer, Observador>> it = observadores.entrySet().iterator();
    while (it.hasNext()) {
        Map.Entry<Integer, Observador> e = it.next();
        try {
            e.getValue().notificarActualizacaoVaga(vagas);   // callback para o cliente
        } catch (org.omg.CORBA.SystemException ex) {
            System.out.println("Observador " + e.getKey() + " inacessível ("
                    + ex.getClass().getSimpleName() + "); a remover");
            it.remove();
        }
    }}





   

    /**
public static void main(String[] args) {

    VagaImpl vIm= new VagaImpl();
    
    //Listar as vagas no parque 1 disponiveis
    VagaDTO[] lista = vIm.listarVagas(1);
    System.out.println(lista.length);
    for( VagaDTO p: lista){
        System.out.println(p.numero_vaga);
        System.out.println(p.estado);
    }
    
    System.out.println("-------------");

    //Listar o numero total de vagas
int total=vIm.numeroTotalVagas(6);
System.out.println("Total de vagas "+total);




    //Adicionar vagas ao parque 6
  // vIm.adicionarVaga(4,20);
    
      //Listar as vagas no parque 6 disponiveis
    lista = vIm.listarVagasDisponiveis(4);

    for( VagaDTO p: lista){
        System.out.println(p.numero_vaga);
        System.out.println(p.estado);
    }



}
        * */


  
}
