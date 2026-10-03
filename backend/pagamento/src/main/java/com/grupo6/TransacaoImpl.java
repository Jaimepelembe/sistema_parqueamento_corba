package com.grupo6;

import com.grupo6.PagamentoApp.TransacaoPOA;

import com.grupo6.PagamentoApp.TransacaoDTO;
import com.grupo6.dao.TransacaoDAO;
import com.grupo6.dao.ContaDAO;


public class TransacaoImpl
        extends TransacaoPOA {
    
    private TransacaoDAO transacaoDAO;


    public TransacaoImpl() {      
    }


    @Override
    public boolean efetuarTransacao(TransacaoDTO transacao){
        boolean resultado=false;
        transacaoDAO = new TransacaoDAO();

        if (transacao.valor>0 && transacao.id_conta>0){
            resultado=transacaoDAO.efetuarTransacao(transacao);
        }

        return resultado;
    }



    @Override
    public TransacaoDTO[] listarTransacoes(int id_usuario) {
        transacaoDAO = new TransacaoDAO();
        ContaDAO contaDAO = new ContaDAO();
        int id_conta=contaDAO.buscarIDConta(id_usuario);//Busca o ID da conta do usuario. 
        
       TransacaoDTO[] listaTransacoes=  transacaoDAO.listarTransacoes(id_conta);

        return listaTransacoes;
    }
    

   

/**
public static void main(String[] args) {
    TransacaoImpl transacao = new TransacaoImpl();
    
    //Listar as Transacoes
    TransacaoDTO[] lista = transacao.listarTransacoes(1);
    
    for( TransacaoDTO p: lista){
        System.out.println(p.tipo);
        System.out.println(p.valor);
    }
    System.out.println("-------------------");
    
    TransacaoDTO transacaoDTO = new TransacaoDTO(-1,"DEPOSITO",600, "CONCLUIDO","03-10-2026","18:14:10",1); //  long id_transacao;
    transacao.EfetuarTransacao(transacaoDTO);


    //Listar as Transacoes
    lista = transacao.listarTransacoes(1);
    
    for( TransacaoDTO p: lista){
        System.out.println(p.tipo);
        System.out.println(p.valor);
    }




}

* */
  



    // restantes métodos...
}
