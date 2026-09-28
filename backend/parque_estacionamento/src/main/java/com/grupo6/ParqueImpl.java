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
    public void adicionarParque(String nome, String provincia, String localizacao, String telefone, String horario, String cobertura, float preco_hora, String foto_url){
        parqueDAO = new ParqueDAO();
        parqueDAO.adicionarParque(String nome, String provincia, String localizacao, String telefone, String horario, String cobertura, float preco_hora, String foto_url);
    }

    @Override
    public void editarParque( int id_parque, String nome, String provincia, String localizacao, String telefone, String horario, String cobertura, float preco_hora, String foto_url) {

        parqueDAO = new ParqueDAO();
        parqueDAO.editarParque(int id_parque, String nome, String provincia, String localizacao, String telefone, String horario, String cobertura, float preco_hora, String foto_url);
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

   

      
public static void main(String[] args) {

    ParqueDAO park = new ParqueDAO();
    //Listar os parques disponiveis
    ParqueDTO[] lista = park.pesquisarPorCategoria("nome");

    for( ParqueDTO p: lista){
        System.out.println(p.nome);
    }

    //Adicionar um parque
    //park.adicionarParque("Machava Km15", "Maputo Provincia", "Machava", "845566871", "24h", "NAO_COBERTO", 10, "imagens/parque_machavakm15.png");
    
       // park.removerParque(5);

        //Listar os parques disponiveis
     lista = park.pesquisarPorCategoria("nome");

    for( ParqueDTO p: lista){
        System.out.println(p.nome);
    }

    //Remover um parque


    //Editar o parque
    park.editarParque( 1,"Machava Socimol2", "Maputo Provincia", "Machava", "845566871", "24h", "NAO_COBERTO", 10, "imagens/parque_machavasocimol.png");
    
    lista = park.pesquisarPorCategoria("nome");

    for( ParqueDTO p: lista){
        System.out.println(p.nome);
    }



}
  



    // restantes métodos...
}
