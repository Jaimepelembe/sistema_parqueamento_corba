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
        if (resultado){
            int id_conta=transacao.id_conta;
            TransacaoDTO[] listaTransacoes= listarTransacoes(id_conta);
            notificarTodos(id_conta,listaTransacoes);

       
        }

        return resultado;
    }



    @Override
    public TransacaoDTO[] listarTransacoes(int id_conta) {
        transacaoDAO = new TransacaoDAO();
        //ContaDAO contaDAO = new ContaDAO();
        //int id_conta=contaDAO.buscarIDConta(id_usuario);//Busca o ID da conta do usuario. 
        
       TransacaoDTO[] listaTransacoes=  transacaoDAO.listarTransacoes(id_conta);

        return listaTransacoes;
    }
    

        @Override
    public int registarObservador(int id_conta,Observador obs){
        synchronized (lock){
            // se o utilizador ainda não tem lista, cria uma; depois adiciona o observador
            List<Observador> lista = observadores.computeIfAbsent(id_conta, k -> new ArrayList<>());
            lista.add(obs);
        }

       // System.out.println("Observador "+id_usuario +"registado (" +total+" no total)");
        return id_usuario;
    }

    @Override 
    public void removerObservador(int id_conta){
        synchronized (lock){
            observadores.remove(id_conta);
        }
       System.out.println("Observador "+id_conta + " removido");
    }


    private void notificarTodos(int id_conta, TransacaoDTO[] listaTransacoes) {
        List<Observador> lista = observadores.get(id_conta);
        if (lista!=null){
            Iterator<Observador> it=lista.iterator();
            while (it.hasNext()){
                Observador obs = it.next();
                
                try{
                obs.notificarActualizacaoTransacao(listaTransacoes); // callback para o cliente
                }catch (org.omg.CORBA.SystemException ex) {
            System.out.println("Observador " + ex + " inacessível ("+ ex.getClass().getSimpleName() + "); a remover");
            it.remove();
        }
            }
        }
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
