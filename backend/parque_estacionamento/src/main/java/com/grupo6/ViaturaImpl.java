package com.grupo6;

import com.grupo6.ParqueamentoApp.ViaturaPOA;
import com.grupo6.ParqueamentoApp.ViaturaDTO;
import com.grupo6.dao.ViaturaDAO;


public class ViaturaImpl
        extends ViaturaPOA {
    
    private ViaturaDAO viaturaDAO;


    public ViaturaImpl() {

        
    }


    @Override
    public void adicionarViatura(ViaturaDTO viatura){
        viaturaDAO = new ViaturaDAO();
        viaturaDAO.adicionarViatura(viatura);
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
