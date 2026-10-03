package com.grupo6.dao;
import com.grupo6.PagamentoApp.ContaDTO;
import java.sql.Connection;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;


public class ContaDAO {
    
    public ContaDAO(){}

    public boolean criarConta(ContaDTO conta){
        boolean resultado=false;
       String sql="INSERT INTO conta(saldo,id_usuario) VALUES (?, ?)";

        try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);

        stmt.setFloat(1, conta.saldo);
        stmt.setInt(2,conta.id_usuario);
        
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


    public boolean depositar(int id_usuario, float valor){
        String sql="UPDATE conta SET saldo=saldo+? WHERE id_usuario=?";
        boolean resultado=false;
           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setFloat(1,valor);
        stmt.setInt(2,id_usuario);
        
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
 

    public boolean debitar(int id_usuario, float valor){
        String sql="UPDATE conta SET saldo=saldo-? WHERE id_usuario=?";
        boolean resultado=false;
           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setFloat(1,valor);
        stmt.setInt(2,id_usuario);
        
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


    public float consultarSaldo(int id_usuario){
        float saldoConta =0;
 
     String sql="SELECT saldo FROM conta WHERE id_usuario=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,id_usuario);
            
            ResultSet rs = stmt.executeQuery();
        
             if (rs.next()){
             
               saldoConta=rs.getFloat("saldo");
            
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
         return saldoConta;// Garante que o método sempre retorne algo

        }

    public int buscarIDConta(int id_usuario){
        int idConta =-1;
 
     String sql="SELECT id_conta FROM conta WHERE id_usuario=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,id_usuario);
            
            ResultSet rs = stmt.executeQuery();
        
             if (rs.next()){
             
               idConta=rs.getInt("id_conta");
            
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
         return idConta;// Garante que o método sempre retorne algo

        }

        

/** 
public static void main(String[] args) {
    ContaDAO c = new ContaDAO();
    float saldo= c.consultarSaldo(1);
    System.out.println("Saldo 1: " +saldo);
    
    c.depositar(1, 600);
    saldo= c.consultarSaldo(1);
    System.out.println("Novo Saldo: " +saldo);
    
    //c.debitar(1, 500);
    //saldo= c.consultarSaldo(1);
    //System.out.println("Novo Saldo -500: " +saldo);

}
**/


    }