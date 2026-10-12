package com.grupo6;

import com.grupo6.ParqueamentoApp.UsuarioPOA;
import com.grupo6.ParqueamentoApp.UsuarioDTO;
import com.grupo6.dao.UsuarioDAO;

import com.grupo6.ParqueamentoApp.Observador;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;


public class UsuarioImpl
        extends UsuarioPOA {
    private final Object lock = new Object();
    private final Map<Integer, Observador> observadores = new HashMap<Integer, Observador>();
    private int proximoId = 1;
    private UsuarioDAO usuarioDAO;


    public UsuarioImpl() {
 

    }



       @Override 
        public UsuarioDTO login(String telefone, String senha){
            synchronized (lock){
            usuarioDAO= new UsuarioDAO();
            UsuarioDTO user= usuarioDAO.login(telefone, senha);

            return user;}
        }

        @Override 
        public void cadastrar (UsuarioDTO usuario){
            synchronized (lock){
            usuarioDAO= new UsuarioDAO();
            usuarioDAO.cadastrar(usuario);}

        }


        public boolean actualizarDados(UsuarioDTO usuario){
            synchronized (lock){
            boolean resultado=false;
                usuarioDAO= new UsuarioDAO();
             
            resultado= usuarioDAO.actualizarDados(usuario);
            if (resultado){
                notificarTodos(usuario);}               
            return resultado;
        
        }
            
        }


        

        @Override
    public int registarObservador(Observador obs){
        int id;
        int total;
        synchronized (lock){
            id=proximoId++;
            observadores.put(id,obs);
            total=observadores.size();
        }

        System.out.println("Observador "+id +"registado (" +total+" no total)");
        return id;
    }

    @Override 
    public void removerObservador(int id){
        synchronized (lock){
            observadores.remove(id);
        }
        System.out.println("Observador "+id + " removido");
    }


    private void notificarTodos(UsuarioDTO usuario) {
    Iterator<Map.Entry<Integer, Observador>> it = observadores.entrySet().iterator();
    while (it.hasNext()) {
        Map.Entry<Integer, Observador> e = it.next();
        try {
            e.getValue().notificarActualizacaoDadosUsuario(usuario);   // callback para o cliente
        } catch (org.omg.CORBA.SystemException ex) {
            System.out.println("Observador " + e.getKey() + " inacessível ("
                    + ex.getClass().getSimpleName() + "); a remover");
            it.remove();
        }
    }}
    
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
    