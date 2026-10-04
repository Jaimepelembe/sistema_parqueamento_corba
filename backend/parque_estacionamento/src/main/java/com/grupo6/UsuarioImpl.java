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
        public void cadastrar (UsuarioDTO usuario){
            usuarioDAO= new UsuarioDAO();
            usuarioDAO.cadastrar(usuario);

        }


        public boolean actualizarDados(UsuarioDTO usuario){
            usuarioDAO= new UsuarioDAO();
             
            return usuarioDAO.actualizarDados(usuario);
            
        }
    
          /**
        public static void main(String[] args){
        UsuarioDTO us = null;
        UsuarioImpl user = new UsuarioImpl();
        us=user.login("841234567", "senha123");
        System.out.println("Login: "+us.nome);
        us = new UsuarioDTO(-1,"Tomas", "840000004", "senha123", 0);

        //Cadastrar um usuario
        user.cadastrar(us);
        us=user.login("840000004", "senha123");
        
        System.out.println("Novo usuario: "+us.nome);
        Integer id=us.id_usuario;
        System.out.println("Id do novo usuario: "+id);
        us=new UsuarioDTO(id, "Tomas Vieira Mario", "840000004", "senha123",-1);
        //Actualizar dados
        boolean resultado= user.actualizarDados(us);
        System.out.println("Login: "+us.nome);
        System.out.println("Resultado: "+resultado);


    }
 
    * */

        }
    