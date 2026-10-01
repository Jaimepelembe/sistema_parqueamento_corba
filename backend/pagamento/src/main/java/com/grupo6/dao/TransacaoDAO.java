package com.grupo6.dao;
import com.grupo6.PagamentoApp.TransacaoDTO;
import java.sql.Connection;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.sql.PreparedStatement;


public class TransacaoDAO {
    
    public TransacaoDAO(){}

    public boolean EfetuarTransacao(TransacaoDTO transacao){
        boolean resultado=false;
       String sql="INSERT INTO transacao (tipo, valor, estado, data,hora,id_conta) VALUES (?, ?, ?, ?, ?, ?)";

        try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setString(1,transacao.tipo);
        stmt.setFloat(2, transacao.valor);
        stmt.setString(3,transacao.estado);
        stmt.setString(4,transacao.data);
        stmt.setString(5,transacao.hora);
        stmt.setInt(6,transacao.id_conta);
        
        int linhasAfectadas=stmt.executeUpdate();
        if (linhasAfectadas>0){
            resultado=true;
        }

        if (!conn.isClosed()) {
                conn.close();}
    }  
        catch (SQLException e){
        System.out.println("Erro de SQL: "+e);
        }  

        catch (Exception e){
            System.out.println("Erro: "+e);

        }
        return resultado;
        }


    public TransacaoDTO[] listarTransacoes(int id_conta){
          //Usamos uma List normal do Java para adicionar os elementos dinamicamente
        List<TransacaoDTO> listaTransacoes=new ArrayList<>();

        String sql="SELECT * FROM transacao WHERE id_conta=?";
            try{
                Connection conn = ConexaoBD.conectar();
                PreparedStatement stmt = conn.prepareStatement(sql);
                stmt.setInt(1,id_conta);
                ResultSet rs = stmt.executeQuery();
            
                while(rs.next()){
                    TransacaoDTO transacao = new TransacaoDTO(
                    rs.getInt("id_transacao"),
                    rs.getString("tipo"),
                    rs.getFloat("valor"),
                    rs.getString("estado"),
                    rs.getString("data"),
                    rs.getString("hora"),
                    rs.getInt("id_conta")
                );
                listaTransacoes.add(transacao); 
        
            }

                if (!conn.isClosed()) {
                    conn.close();}

        }
            catch (Exception e){
                System.out.println("Erro: "+e);

            }
            
            TransacaoDTO[] listTransacoesDTO = listaTransacoes.toArray(new TransacaoDTO[0]); //Converte o ArrayList em um array simples.

            return listTransacoesDTO;// Garante que o método sempre retorne algo (o objeto montado ou a lista vazia)

            }




        

/**
public static void main(String[] args) {
    TransacaoDAO c = new TransacaoDAO();
    //TransacaoDTO t = new TransacaoDTO(-1,"Deposito",500,"CONCLUIDO","2026-10-01","23:45",1);
    TransacaoDTO[] transacoes= c.listarTransacoes(1);
    //c.EfetuarTransacao(t);
    for(TransacaoDTO transacao: transacoes){
        System.out.println(transacao.id_conta);
        System.out.println(transacao.estado);
        System.out.println(transacao.data);
        System.out.println(transacao.hora);

        


    }
    
    //c.debitar(1, 500);
    //saldo= c.consultarSaldo(1);
    //System.out.println("Novo Saldo -500: " +saldo);

}

* */

  }



  