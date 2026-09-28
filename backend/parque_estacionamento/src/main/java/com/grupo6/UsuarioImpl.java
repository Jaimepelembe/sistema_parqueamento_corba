package com.grupo6;

import com.grupo6.ParqueamentoApp.UsuarioPOA;
import com.grupo6.ParqueamentoApp.UsuarioDTO;
import com.grupo6.dao.UsuarioDAO;



public class UsuarioImpl
        extends UsuarioPOA {
    
    private UsuarioDAO usuarioDAO;


    public UsuarioImpl() {
 

    }



       @Override 
        public UsuarioDTO login(String telefone, String senha){
            usuarioDAO= new UsuarioDAO();
            UsuarioDTO user= usuarioDAO.login(telefone, senha);

            return user;
        }

        @Override 
        public void cadastrar (String nome, String telefone, String senha, int tipo){
            usuarioDAO= new UsuarioDAO();
            usuarioDAO.cadastrar(nome, telefone,senha,tipo);

        }


        public UsuarioDTO actualizarDados(int id_usuario, String nome, String telefone, String senha){
            usuarioDAO= new UsuarioDAO();
            UsuarioDTO user= usuarioDAO.actualizarDados(id_usuario,nome, telefone,senha);
            
            return user;
            
        }
        /**
   
        public static void main(String[] args){
        //Inicializar as tabelas caso elas nao existam
        UsuarioDTO us = null;
        UsuarioImpl user = new UsuarioImpl();
        us=user.login("841234567", "senha123");
        System.out.println("Login: "+us.nome);
        

        //Cadastrar um usuario
        user.cadastrar("Gabriel", "840000003", "senha123", 0);
        us=user.login("840000003", "senha123");
        
        System.out.println("Novo usuario: "+us.nome);
        Integer id=us.idUsuario;
        System.out.println("Novo usuario: "+id);
        
        //Actualizar dados
        us= user.actualizarDados(id, "Matheus Jesus", "840000003", "senha123");
        System.out.println("Dado actualizado: "+us.nome);


    }* */

        }
    