package com.grupo6;

import com.grupo6.PagamentoApp.ContaDTO;
import com.grupo6.PagamentoApp.ContaPOA;
import com.grupo6.dao.ContaDAO;


public class ContaImpl
        extends ContaPOA {

    private ContaDAO contaDAO;

    public ContaImpl() {

        
    }


    @Override
    public boolean criarConta(ContaDTO conta){
        boolean resultado=false;
        if (conta.saldo>=0 && conta.id_usuario>0){
        contaDAO = new ContaDAO();
        resultado=contaDAO.criarConta(conta);
        }
        return resultado;
    }


    @Override
    public float consultarSaldo(int id_usuario){
        contaDAO = new ContaDAO();
        float saldoConta= contaDAO.consultarSaldo(id_usuario);
        return saldoConta;
    }





      @Override
      public int buscarIDConta(int id_usuario){
        contaDAO = new ContaDAO();
        int idConta= contaDAO.buscarIDConta(id_usuario);
        return idConta;

      }


     @Override
    public boolean debitar(int id_usuario, float valor){
        boolean resultado=false;
        float saldoActual=consultarSaldo(id_usuario);

        contaDAO = new ContaDAO();
        if (id_usuario>0 && saldoActual >= valor){
            resultado= contaDAO.debitar(id_usuario,valor);}
  
        return resultado;
    }

    @Override
    public boolean depositar(int id_usuario, float valor){
        boolean resultado=false;

        contaDAO = new ContaDAO();
        if (id_usuario>0 && valor > 0){
            resultado= contaDAO.depositar(id_usuario,valor);}
  
        return resultado;
    }

   

 /**   
public static void main(String[] args) {

    ContaImpl c = new ContaImpl();
    //ContaDTO conta= new ContaDTO(-1,100,11);
    
   // c.criarConta(conta);
    
    float saldo= c.consultarSaldo(12);
    System.out.println("Saldo 1: " +saldo);
    
    //c.depositar(11, 600);
    saldo= c.consultarSaldo(12);
    System.out.println("Novo Saldo: " +saldo);
    

    //c.debitar(1, 150);
    //saldo= c.consultarSaldo(1);
    System.out.println("Novo Saldo: " +saldo);



}


* */
  



    // restantes métodos...
}
