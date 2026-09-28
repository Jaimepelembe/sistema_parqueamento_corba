package com.grupo6.dao;
import com.grupo6.ParqueamentoApp.UsuarioDTO;
import java.sql.Connection;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
//import java.sql.SQLException;

public class UsuarioDAO {
    
    public UsuarioDAO(){}

    public void cadastrar(String nome, String telefone,String senha,Integer tipo){
        String sql="INSERT INTO usuario (nome, telefone, senha, tipo) VALUES (?, ?, ?, ?)";

           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setString(1,nome);
        stmt.setString(2,telefone);
        stmt.setString(3,senha);
        stmt.setInt(4,tipo);
        
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


    public UsuarioDTO login(String telefone, String senha){
        UsuarioDTO usuario =null;
 
     String sql="SELECT id_usuario,nome,telefone,tipo FROM usuario WHERE telefone=? AND senha=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1,telefone);
            stmt.setString(2,senha);
            
            ResultSet rs = stmt.executeQuery();
        
             if (rs.next()){
             
               usuario= new UsuarioDTO(
                    rs.getInt("id_usuario"),
                    rs.getString("nome"),
                    rs.getString("telefone"),
                    rs.getInt("tipo"));
            
    
        }

            if (!conn.isClosed()) {
                conn.close();}

    }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
         return usuario;// Garante que o método sempre retorne algo (o objeto montado ou null)

        }
        

    public UsuarioDTO actualizarDados(Integer id_usuario,String nome, String telefone, String senha){
        UsuarioDTO usuario =null;

             String sql="UPDATE usuario SET nome=?,telefone=?,senha=? WHERE id_usuario=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1,nome);
            stmt.setString(2,telefone);
            stmt.setString(3,senha);
            stmt.setInt(4,id_usuario);
            
            Integer linhasAfectadas = stmt.executeUpdate();
            if (linhasAfectadas>0){
                usuario = new UsuarioDTO(id_usuario,nome,telefone,0);
            }

            if (!conn.isClosed()) {
                conn.close();}


    } catch (SQLException e){
            System.out.println("Erro de SQL: "+e);

        }
        catch (Exception e){
            System.out.println("Erro: "+e);

        }
         return usuario;// Garante que o método sempre retorne algo (o objeto montado ou null)

    }

    }



