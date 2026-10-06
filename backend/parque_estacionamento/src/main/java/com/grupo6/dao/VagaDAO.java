package com.grupo6.dao;

import com.grupo6.ParqueamentoApp.VagaDTO;
import java.sql.Connection;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.List;



public class VagaDAO {

    public VagaDAO(){}

  public void  adicionarVaga (VagaDTO vaga){
      String sql="INSERT INTO vaga_estacionamento (numero_vaga,estado,id_parque) VALUES (?,?,?)";

           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setString(1,vaga.numero_vaga);
        stmt.setInt(2,vaga.estado);
        stmt.setInt(3,vaga.id_parque);

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

      public boolean actualizarEstadoVaga(int id_vaga, int estadoVaga){
        boolean resultado =false;

             String sql="UPDATE vaga_estacionamento SET estado=? WHERE id_vaga=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,estadoVaga);
            stmt.setInt(2,id_vaga);
            
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
         return resultado;// Garante que o método sempre retorne algo (o objeto montado ou null)

    }




public VagaDTO[] listarVagas (int id_parque){
    //Usamos uma List normal do Java para adicionar os elementos dinamicamente
    List<VagaDTO> listaVagas=new ArrayList<>();

     String sql="SELECT * FROM vaga_estacionamento WHERE id_parque=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,id_parque);
  
            ResultSet rs = stmt.executeQuery();
        
             while(rs.next()){
                VagaDTO vaga = new VagaDTO(
                rs.getInt("id_vaga"),
                rs.getString("numero_vaga"),
                rs.getInt("estado"),
                rs.getInt("id_parque")
                );
            listaVagas.add(vaga); 
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
        
        VagaDTO[] listaVagasDTO = listaVagas.toArray(new VagaDTO[0]); //Converte o ArrayList em um array simples.

        return listaVagasDTO;// Garante que o método sempre retorne algo (o objeto montado ou a lista vazia)

        }



public VagaDTO[] listarVagasDisponivies (int id_parque){
    //Usamos uma List normal do Java para adicionar os elementos dinamicamente
    List<VagaDTO> listaVagas=new ArrayList<>();

     String sql="SELECT * FROM vaga_estacionamento WHERE id_parque=? AND estado=0";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,id_parque);
  
            ResultSet rs = stmt.executeQuery();
        
             while(rs.next()){
                VagaDTO vaga = new VagaDTO(
                rs.getInt("id_vaga"),
                rs.getString("numero_vaga"),
                rs.getInt("estado"),
                rs.getInt("id_parque")
                );
            listaVagas.add(vaga); 
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
        
        VagaDTO[] listaVagasDTO = listaVagas.toArray(new VagaDTO[0]); //Converte o ArrayList em um array simples.

        return listaVagasDTO;// Garante que o método sempre retorne algo (o objeto montado ou a lista vazia)

        }


        
public int numeroTotalVagas (int id_parque){
    //Usamos uma List normal do Java para adicionar os elementos dinamicamente
    int numeroTotal=0;

     String sql="SELECT COUNT(id_vaga) AS total FROM vaga_estacionamento WHERE id_parque=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,id_parque);
  
            ResultSet rs = stmt.executeQuery();
        
             while(rs.next()){
               numeroTotal=rs.getInt("total");
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
        
       

        return numeroTotal;

        }
        



}

