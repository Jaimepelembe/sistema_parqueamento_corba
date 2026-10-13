package com.grupo6;

import com.grupo6.ParqueamentoApp.ViaturaPOA;
import com.grupo6.ParqueamentoApp.ViaturaDTO;
import com.grupo6.dao.ViaturaDAO;

import com.grupo6.ParqueamentoApp.Observador;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import java.util.ArrayList;
import java.util.List;



public class ViaturaImpl
        extends ViaturaPOA {
    private final Object lock = new Object();
    private final Map<Integer, List<Observador>> observadores = new HashMap<Integer, List<Observador>>();
    private ViaturaDAO viaturaDAO;


    public ViaturaImpl() {

        
    }


    @Override
    public void adicionarViatura(ViaturaDTO viatura){
        synchronized (lock){
        viaturaDAO = new ViaturaDAO();
        viaturaDAO.adicionarViatura(viatura);
        
        //Envia notificacao ao observador
        ViaturaDTO[] viaturas=listarViaturas(viatura.id_usuario);
        notificarTodos(viatura.id_usuario,viaturas);

    }
    }



    @Override
    public ViaturaDTO[] listarViaturas(int id_usuario) {
         viaturaDAO = new ViaturaDAO();
        
        ViaturaDTO[] listaViaturass=  viaturaDAO.listarViaturas(id_usuario);

        return listaViaturass;}
    

    @Override
    public void removerViatura( int id_viatura){
        viaturaDAO = new ViaturaDAO();
        viaturaDAO.removerViatura(id_viatura);
    }


            @Override
    public int registarObservador(int id_usuario,Observador obs){
        //int total;
        synchronized (lock){
            // se o utilizador ainda não tem lista, cria uma; depois adiciona o observador
            List<Observador> lista = observadores.computeIfAbsent(id_usuario, k -> new ArrayList<>());
            lista.add(obs);

            //observadores.put(id_usuario,obs);
            //total=observadores.size();
        }

       // System.out.println("Observador "+id_usuario +"registado (" +total+" no total)");
        return id_usuario;
    }

    @Override 
    public void removerObservador(int id){
        synchronized (lock){
            observadores.remove(id);
        }
        System.out.println("Observador "+id + " removido");
    }


    private void notificarTodos(int id_usuario,ViaturaDTO[] viaturas) {
        List<Observador> lista = observadores.get(id_usuario);
        if (lista!=null){
            Iterator<Observador> it=lista.iterator();
            while (it.hasNext()){
                Observador obs = it.next();
                
                try{
                obs.notificarActualizacaoViaturas(viaturas); // callback para o cliente
                }catch (org.omg.CORBA.SystemException ex) {
            System.out.println("Observador " + ex + " inacessível ("+ ex.getClass().getSimpleName() + "); a remover");
            it.remove();
        }
            }


        }


}

   

    /**
public static void main(String[] args) {

    ViaturaImpl viatura = new ViaturaImpl();
    //Listar os parques disponiveis
    ViaturaDTO[] lista = viatura.listarViaturas(1);

    for( ViaturaDTO p: lista){
        System.out.println(p.marca);
        System.out.println(p.modelo);
    }
System.out.println("-------------------");

    //Adicionar uma viatura
    ViaturaDTO v1= new ViaturaDTO(-1,"Porche","Panamera","ABC-102",1);
    viatura.adicionarViatura(v1);
    
       // park.removerParque(5);

        //Listar as viaturas disponiveis
     lista = viatura.listarViaturas(1);

    for( ViaturaDTO p: lista){
        System.out.println(p.marca);
        System.out.println(p.modelo);
        System.out.println(p.id_viatura);
        
    }

    System.out.println("-------------------");
    //Remover uma viatura

    viatura.removerViatura(1);

    for( ViaturaDTO p: lista){
        System.out.println(p.marca);
        System.out.println(p.modelo);
        System.out.println(p.id_viatura);
    }




}


* */
  



    // restantes métodos...
}
