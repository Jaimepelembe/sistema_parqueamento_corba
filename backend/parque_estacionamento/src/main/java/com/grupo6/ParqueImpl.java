package com.grupo6;

import com.grupo6.ParqueamentoApp.ParquePOA;
import com.grupo6.ParqueamentoApp.ParqueDTO;
import com.grupo6.dao.ParqueDAO;
import com.grupo6.ParqueamentoApp.Observador;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class ParqueImpl
        extends ParquePOA {
    private final Object lock = new Object();
    private final Map<Integer, Observador> observadores = new HashMap<Integer, Observador>();
    private int proximoId = 1;
    
    private ParqueDAO parqueDAO;


    public ParqueImpl() {

        
    }


    @Override
    public int adicionarParque(ParqueDTO parque){
        synchronized(lock){
        parqueDAO = new ParqueDAO();
        return parqueDAO.adicionarParque(parque);
    }
    }

    @Override
    public boolean editarParque(ParqueDTO parque) {
        synchronized(lock){
        parqueDAO = new ParqueDAO();
        
    return parqueDAO.editarParque(parque);   } 
    }


        @Override
    public ParqueDTO[] pesquisarPorCategoria(String categoria) {
        parqueDAO = new ParqueDAO();
        ParqueDTO[] listaParques=  parqueDAO.pesquisarPorCategoria(categoria);

        return listaParques;}
    

    @Override
    public boolean removerParque( int id_parque){
        parqueDAO = new ParqueDAO();
        return parqueDAO.removerParque(id_parque);
    }

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


    private void notificarTodos(ParqueDTO[] parques) {
    Iterator<Map.Entry<Integer, Observador>> it = observadores.entrySet().iterator();
    while (it.hasNext()) {
        Map.Entry<Integer, Observador> e = it.next();
        try {
            e.getValue().notificarParquesActualizados(parques);   // callback para o cliente
        } catch (org.omg.CORBA.SystemException ex) {
            System.out.println("Observador " + e.getKey() + " inacessível ("
                    + ex.getClass().getSimpleName() + "); a remover");
            it.remove();
        }
    }
}
   

      /**
public static void main(String[] args) {

    ParqueDAO park = new ParqueDAO();
    //Listar os parques disponiveis
    ParqueDTO[] lista = park.pesquisarPorCategoria("nome");

    for( ParqueDTO p: lista){
        System.out.println(p.nome);
    }

    //Adicionar um parque
    ParqueDTO par= new ParqueDTO(-1,"Machava Km18", "Maputo Provincia", "Machava", "845566871", "24h", "NAO_COBERTO", 10, "imagens/parque_machavakm18.png");

    park.adicionarParque(par);
    
       // park.removerParque(5);

        //Listar os parques disponiveis
     lista = park.pesquisarPorCategoria("nome");

    for( ParqueDTO p: lista){
        System.out.println(p.nome);
    }

    //Remover um parque

    par = new ParqueDTO(1,"Machava Socimol 25", "Maputo Provincia", "Machava", "845566871", "24h", "NAO_COBERTO", 10, "imagens/parque_machavasocimol.png");
    //Editar o parque
    park.editarParque(par);
    
    lista = park.pesquisarPorCategoria("nome");

    for( ParqueDTO p: lista){
        System.out.println(p.nome);
    }



}

* */
  



    // restantes métodos...
}
