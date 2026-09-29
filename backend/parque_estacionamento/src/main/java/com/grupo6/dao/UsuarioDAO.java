package com.grupo6.dao;
import com.grupo6.ParqueamentoApp.UsuarioDTO;
import java.sql.Connection;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;


public class UsuarioDAO {
    
    public UsuarioDAO(){}

    public void cadastrar(UsuarioDTO usuario){
        String sql="INSERT INTO usuario (nome, telefone, senha, tipo) VALUES (?, ?, ?, ?)";

           try{
        Connection conn = ConexaoBD.conectar();
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setString(1,usuario.nome);
        stmt.setString(2,usuario.telefone);
        stmt.setString(3,usuario.senha);
        stmt.setInt(4,usuario.tipo);
        
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
                    null,
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
        

    public boolean actualizarDados(UsuarioDTO usuarioDTO){
        boolean resultado =false;

             String sql="UPDATE usuario SET nome=?,telefone=?,senha=? WHERE id_usuario=?";
        try{
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1,usuarioDTO.nome);
            stmt.setString(2,usuarioDTO.telefone);
            stmt.setString(3,usuarioDTO.senha);
            stmt.setInt(4,usuarioDTO.id_usuario);
            
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

    }



