package com.grupo6;

import com.grupo6.ParqueamentoApp.VagaPOA;
import com.grupo6.ParqueamentoApp.VagaDTO;
import com.grupo6.dao.VagaDAO;


public class VagaImpl extends VagaPOA {
    
    private VagaDAO vagaDAO;


    public VagaImpl() {

        
    }



    public void adicionarVaga(int id_parque, int numero_de_vagas){
        vagaDAO= new VagaDAO();
        VagaDTO vaga= null;

        for ( int i=0; i<numero_de_vagas;i++){
           String numero="A-"+(i+1);
           //System.out.println(numero);
            vaga = new VagaDTO(-1,numero, 0, id_parque);
            vagaDAO.adicionarVaga(vaga);
        }
    }

    public boolean actualizarEstadoVaga(int id_vaga, int estadoVaga){
        vagaDAO= new VagaDAO();
        boolean resultado=false;
        resultado=vagaDAO.actualizarEstadoVaga(id_vaga, estadoVaga);

        return resultado;
    }

    
    public VagaDTO[] listarVagas(int id_parque) {
        vagaDAO = new VagaDAO();
        VagaDTO[] listaVagas=   vagaDAO.listarVagas(id_parque);

        return listaVagas;}


@Override 
public VagaDTO[] listarVagasDisponiveis(int id_parque) {
    vagaDAO = new VagaDAO();
    VagaDTO[] listaVagas=   vagaDAO.listarVagasDisponivies(id_parque);

    return listaVagas;}


    
@Override 
public int numeroTotalVagas(int id_parque) {
    int numeroTotal=0;
    vagaDAO = new VagaDAO();
    numeroTotal= vagaDAO.numeroTotalVagas(id_parque);

    return numeroTotal;}





   

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
