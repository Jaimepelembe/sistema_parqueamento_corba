package com.grupo6.dao;

import com.grupo6.ParqueamentoApp.ViaturaDTO;
import java.sql.Connection;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.List;



public class ViaturaDAO {

    public ViaturaDAO(){}

  public void  adicionarViatura (ViaturaDTO viatura){
      String sql="INSERT INTO viatura (marca, modelo, matricula,id_usuario) VALUES (?,?,?,?)";

           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setString(1,viatura.marca);
        stmt.setString(2,viatura.modelo);
        stmt.setString(3,viatura.matricula);
        stmt.setInt(4,viatura.id_usuario);

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



public ViaturaDTO[] listarViaturas (int id_usuario){
    //Usamos uma List normal do Java para adicionar os elementos dinamicamente
    List<ViaturaDTO> listaViaturas=new ArrayList<>();

     String sql="SELECT * FROM viatura WHERE id_usuario=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,id_usuario);
            ResultSet rs = stmt.executeQuery();
        
             while(rs.next()){
                ViaturaDTO viatura = new ViaturaDTO(
                rs.getInt("id_viatura"),
                rs.getString("marca"),
                rs.getString("modelo"),
                rs.getString("matricula"),
                rs.getInt("id_usuario")
            );
            listaViaturas.add(viatura); 
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
        
        ViaturaDTO[] listViaturasDTO = listaViaturas.toArray(new ViaturaDTO[0]); //Converte o ArrayList em um array simples.

        return listViaturasDTO;// Garante que o método sempre retorne algo (o objeto montado ou a lista vazia)

        }

public void removerViatura (int id_viatura){

          String sql="DELETE FROM viatura WHERE id_viatura=?";

           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setInt(1,id_viatura);
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

