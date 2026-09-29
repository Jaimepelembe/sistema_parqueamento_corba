package com.grupo6;

import com.grupo6.ParqueamentoApp.ParquePOA;
import com.grupo6.ParqueamentoApp.ParqueDTO;
import com.grupo6.dao.ParqueDAO;


public class ParqueImpl
        extends ParquePOA {
    
    private ParqueDAO parqueDAO;


    public ParqueImpl() {

        
    }


    @Override
    public void adicionarParque(ParqueDTO parque){
        parqueDAO = new ParqueDAO();
        parqueDAO.adicionarParque(parque);
    }

    @Override
    public boolean editarParque(ParqueDTO parque) {

        parqueDAO = new ParqueDAO();
        
    return parqueDAO.editarParque(parque);    
    }


        @Override
    public ParqueDTO[] pesquisarPorCategoria(String categoria) {
        parqueDAO = new ParqueDAO();
        ParqueDTO[] listaParques=  parqueDAO.pesquisarPorCategoria(categoria);

        return listaParques;}
    

    @Override
    public void removerParque( int id_parque){
        parqueDAO = new ParqueDAO();
        parqueDAO.removerParque(id_parque);


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
