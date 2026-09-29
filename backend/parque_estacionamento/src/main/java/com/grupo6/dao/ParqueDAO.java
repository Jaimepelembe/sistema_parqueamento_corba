package com.grupo6.dao;

import com.grupo6.ParqueamentoApp.ParqueDTO;
import java.sql.Connection;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.List;



public class ParqueDAO {

    public ParqueDAO(){}

  public void  adicionarParque (ParqueDTO parque){
      String sql="INSERT INTO parque_estacionamento (nome, provincia, localizacao,telefone,horario,cobertura,preco, foto_url) VALUES (?,?,?,?,?,?,?,?)";

           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setString(1,parque.nome);
        stmt.setString(2,parque.provincia);
        stmt.setString(3,parque.localizacao);
        stmt.setString(4,parque.telefone);
        stmt.setString(5,parque.horario);
        stmt.setString(6,parque.cobertura);
        stmt.setFloat(7,parque.preco);
        stmt.setString(8,parque.foto_url);

        stmt.executeUpdate();


        if (!conn.isClosed()) {
                conn.close();}
    }  
        catch (SQLException e){
        System.out.println("Erro de SQL: "+e);
        }  

        catch (Exception e){
            System.out.println("Erro: "+e);

        }


  }


  public boolean editarParque (ParqueDTO parque){

           boolean resultado =false;
     

             String sql="UPDATE parque_estacionamento SET nome=?,provincia=?,localizacao=?,telefone=?,horario=?,cobertura=?,preco=?,foto_url=? WHERE id_parque=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1,parque.nome);
            stmt.setString(2,parque.provincia);
            stmt.setString(3,parque.localizacao);
            stmt.setString(4,parque.telefone);
            stmt.setString(5,parque.horario);
            stmt.setString(6,parque.cobertura);
            stmt.setFloat(7,parque.preco);
            stmt.setString(8,parque.foto_url);
            stmt.setInt(9,parque.id_parque);
            
            int linhasAfectadas = stmt.executeUpdate();
            if (linhasAfectadas>0){
                resultado = true;
            }

            if (!conn.isClosed()) {
                conn.close();}


    } catch (SQLException e){
            System.out.println("Erro de SQL: "+e);

        }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }

        return resultado;

    }


public ParqueDTO[] pesquisarPorCategoria (String categoria){
    //Usamos uma List normal do Java para adicionar os elementos dinamicamente
    List<ParqueDTO> listaParques=new ArrayList<>();

     String sql="SELECT * FROM parque_estacionamento ORDER BY "+categoria +" ASC";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
  
            ResultSet rs = stmt.executeQuery();
        
             while(rs.next()){
                ParqueDTO parque = new ParqueDTO(
                rs.getInt("id_parque"),
                rs.getString("nome"),
                rs.getString("provincia"),
                rs.getString("localizacao"),
                rs.getString("telefone"),
                rs.getString("horario"),
                rs.getString("cobertura"),
                rs.getFloat("preco"),
                rs.getString("foto_url")
            )             ;
            listaParques.add(parque); 
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
        
        ParqueDTO[] listaParquesDTO = listaParques.toArray(new ParqueDTO[0]); //Converte o ArrayList em um array simples.

        return listaParquesDTO;// Garante que o método sempre retorne algo (o objeto montado ou a lista vazia)

        }

public void removerParque (int id_parque){

          String sql="DELETE FROM parque_estacionamento WHERE id_parque=?";

           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setInt(1,id_parque);
        stmt.executeUpdate();


        if (!conn.isClosed()) {
                conn.close();}
    }  
        catch (SQLException e){
        System.out.println("Erro de SQL: "+e);
        }  

        catch (Exception e){
            System.out.println("Erro: "+e);

        }

};




}

