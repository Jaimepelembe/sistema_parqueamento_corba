package com.grupo6;

import com.grupo6.ParqueamentoApp.UsuarioPOA;
import com.grupo6.ParqueamentoApp.UsuarioDTO;
import com.grupo6.dao.UsuarioDAO;

import com.grupo6.ParqueamentoApp.Observador;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import java.util.ArrayList;
import java.util.List;


public class UsuarioImpl
        extends UsuarioPOA {
    private final Object lock = new Object();
    private final Map<Integer, List<Observador>> observadores = new HashMap<Integer, List<Observador>>();
    //private int proximoId = 1;
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
    public int registarObservador(int id_usuario,Observador obs){
        //int total;
        synchronized (lock){
            // se o utilizador ainda não tem lista, cria uma; depois adiciona o observador
            List<Observador> lista = observadores.computeIfAbsent(id_usuario, k -> new ArrayList<>());
            lista.add(obs);

            //observadores.put(id_usuario,obs);
            //total=observadores.size();
        }

       // System.out.println("Observador "+id_usuario +"registado (" +total+" no total)");
        return id_usuario;
    }

    @Override 
    public void removerObservador(int id){
        synchronized (lock){
            observadores.remove(id);
        }
        System.out.println("Observador "+id + " removido");
    }


    private void notificarTodos(UsuarioDTO usuario) {
        List<Observador> lista = observadores.get(usuario.id_usuario);
        if (lista!=null){
            Iterator<Observador> it=lista.iterator();
            while (it.hasNext()){
                Observador obs = it.next();
                
                try{
                obs.notificarActualizacaoDadosUsuario(usuario); // callback para o cliente
                }catch (org.omg.CORBA.SystemException ex) {
            System.out.println("Observador " + ex + " inacessível ("+ ex.getClass().getSimpleName() + "); a remover");
            it.remove();
        }
            }


        }


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
    