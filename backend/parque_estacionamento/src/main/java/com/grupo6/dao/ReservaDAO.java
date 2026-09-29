package com.grupo6.dao;

import com.grupo6.ParqueamentoApp.ReservaDTO;
import java.sql.Connection;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.List;



public class ReservaDAO {

    public ReservaDAO(){}

  public void  criarReserva (ReservaDTO reserva){
      String sql="INSERT INTO reserva_vaga (data_entrada, hora_entrada, data_saida,hora_saida,preco_total,id_vaga,id_usuario,id_viatura) VALUES (?,?,?,?,?,?,?,?)";

           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setString(1,reserva.data_entrada);
        stmt.setString(2,reserva.hora_entrada);
        stmt.setString(3,reserva.data_saida);
        stmt.setString(4,reserva.hora_saida);
        stmt.setFloat(5,reserva.preco_total);
        stmt.setInt(6,reserva.id_vaga);
        stmt.setInt(7,reserva.id_usuario);
        stmt.setInt(8,reserva.id_viatura);

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



public ReservaDTO obterReserva (int id_reserva){
    //Usamos uma List normal do Java para adicionar os elementos dinamicamente
    ReservaDTO reserva=null;

     String sql="SELECT * FROM reserva WHERE id_reserva=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,id_reserva);
            ResultSet rs = stmt.executeQuery();
        
            while(rs.next()){
                reserva = new ReservaDTO(
                    rs.getInt("id_reserva"),
                    rs.getString("data_entrada"),
                    rs.getString("hora_entrada"),
                    rs.getString("data_saida"),
                    rs.getString("hora_saida"),
                    rs.getFloat("preco_total"),
                    rs.getInt("id_vaga"),
                    rs.getInt("id_usuario"),
                    rs.getInt("id_viatura")
            );
            
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
        
       
        return reserva;// 

        }


public ReservaDTO[] listarReservas (int id_usuario){
    //Usamos uma List normal do Java para adicionar os elementos dinamicamente
    List<ReservaDTO> listaReservas=new ArrayList<>();

     String sql="SELECT * FROM reserva_vaga WHERE id_usuario=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,id_usuario);
            ResultSet rs = stmt.executeQuery();
        
             while(rs.next()){
                ReservaDTO reserva = new ReservaDTO(
                    rs.getInt("id_reserva"),
                    rs.getString("data_entrada"),
                    rs.getString("hora_entrada"),
                    rs.getString("data_saida"),
                    rs.getString("hora_saida"),
                    rs.getFloat("preco_total"),
                    rs.getInt("id_vaga"),
                    rs.getInt("id_usuario"),
                    rs.getInt("id_viatura")
            );
            listaReservas.add(reserva); 
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
        
        ReservaDTO[] listReservasDTO = listaReservas.toArray(new ReservaDTO[0]); //Converte o ArrayList em um array simples.

        return listReservasDTO;// Garante que o método sempre retorne algo (o objeto montado ou a lista vazia)

        }


public float obterPrecoHoraParque(int id_vaga){
    float preco_parque=0;

     String sql="SELECT p.preco FROM parque_estacionamento p JOIN vaga_estacionamento v ON p.id_parque = v.id_parque WHERE v.id_vaga = ?";

     
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1,id_vaga);
            ResultSet rs = stmt.executeQuery();
        
             while(rs.next()){
                preco_parque=rs.getFloat("preco");
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
        
  

        return preco_parque;

        }





}

