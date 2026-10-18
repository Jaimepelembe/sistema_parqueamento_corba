package com.grupo6;

import com.grupo6.ParqueamentoApp.ReservaPOA;

import java.time.LocalDateTime;
import java.time.Duration;

import com.grupo6.ParqueamentoApp.ReservaDTO;
import com.grupo6.dao.ReservaDAO;

import com.grupo6.ParqueamentoApp.Observador;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import java.util.ArrayList;
import java.util.List;


public class ReservaImpl
        extends ReservaPOA {
    private final Object lock = new Object();
    private final Map<Integer, List<Observador>> observadores = new HashMap<Integer, List<Observador>>();
    private ReservaDAO reservaDAO;


    public ReservaImpl() {

        
    }


    @Override
    public boolean criarReserva(ReservaDTO reserva){
        reservaDAO = new ReservaDAO();
        boolean resultado=reservaDAO.criarReserva(reserva);
        
        if (resultado){
            int id_usuario=reserva.id_usuario;
            ReservaDTO[] listaReservas= listarReservas(id_usuario);
            notificarTodos(id_usuario,listaReservas);
        }


       return resultado;
    }



        @Override
    public ReservaDTO[] listarReservas(int id_usuario) {
         reservaDAO = new ReservaDAO();
        
        ReservaDTO[] listaReservas=  reservaDAO.listarReservas(id_usuario);

        return listaReservas;}
    
    @Override
     public boolean actualizarStatusReserva(ReservaDTO reserva ){
        reservaDAO = new ReservaDAO();
        boolean resultado=reservaDAO.actualizarStatusReserva(reserva );
       return resultado;


     }


     @Override
     public boolean actualizarStatusReservaNotificacao(ReservaDTO reserva ){
        reservaDAO = new ReservaDAO();
        boolean resultado=reservaDAO.actualizarStatusReserva(reserva );
        
        if (resultado){
            ReservaDTO[] listaReservas= listarReservas(reserva.id_usuario);
            notificarTodos(reserva.id_usuario,listaReservas);
        }


       return resultado;


     }


    @Override
    public ReservaDTO obterReserva(int id_reserva) {
         reservaDAO = new ReservaDAO();
        
        ReservaDTO reserva=  reservaDAO.obterReserva(id_reserva);

        return reserva;}

    


    @Override
    public int registarObservador(int id_usuario,Observador obs){
        synchronized (lock){
            // se o utilizador ainda não tem lista, cria uma; depois adiciona o observador
            List<Observador> lista = observadores.computeIfAbsent(id_usuario, k -> new ArrayList<>());
            lista.add(obs);
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


    private void notificarTodos(int id_usuario, ReservaDTO[] reservas) {
        List<Observador> lista = observadores.get(id_usuario);
        if (lista!=null){
            Iterator<Observador> it=lista.iterator();
            while (it.hasNext()){
                Observador obs = it.next();
                
                try{
                obs.notificarActualizacaoReservas(reservas); // callback para o cliente
                }catch (org.omg.CORBA.SystemException ex) {
            System.out.println("Observador " + ex + " inacessível ("+ ex.getClass().getSimpleName() + "); a remover");
            it.remove();
        }
            }
        }
}

    
    public long calcularTempoReserva(String data_entrada,String hora_entrada,String data_saida,String hora_saida){
        long tempoTotal=0;

        //Unir as strings no formato padronizado ISO (YYYY-MM-DDTHH:MM:SS)
        String inicioStr = data_entrada + "T" + hora_entrada;
        String fimStr = data_saida + "T" + hora_saida;

        // 2. Converter de String para LocalDateTime
        LocalDateTime inicio = LocalDateTime.parse(inicioStr);
        LocalDateTime fim = LocalDateTime.parse(fimStr);

        // 3. Calcular a duração entre as duas datas
        Duration duracao = Duration.between(inicio, fim);

        // 4. Extrair os dias, horas e minutos
        //long totalDias = duracao.toDays();
        //long horasRestantes = duracao.toHours() % 24;
        //long minutosRestantes = duracao.toMinutes() % 60;

        // Exibir o resultado formatado
        //System.out.println("Tempo total: " + totalDias + " dia(s), " + horasRestantes + " hora(s) e " + minutosRestantes + " minuto(s)");
       // System.out.println("Total absoluto em horas: " + duracao.toHours() + " horas");
    
        tempoTotal=duracao.toHours();
        return tempoTotal;

    }
   

   /**
public static void main(String[] args) {
    ReservaDAO reservaDAO = new ReservaDAO();


    ReservaImpl res=new ReservaImpl();
    //long total =res.calcularTempoReserva("2026-09-25","08:30:00","2026-09-29","14:45:00");
    //System.out.println(total);
   // ReservaDTO reserva= new ReservaDTO(-1,"2026-09-25","08:30:00","2026-09-29","14:45:00",0,2,4,4);
    //res.criarReserva(reserva);
    //float preco=reservaDAO.obterPrecoHoraParque(1);
    //System.out.println(preco);

   ReservaDTO[] reservas = res.listarReservas(4);
   for( int i=0; i<reservas.length;i++){
    System.out.println(reservas[i].data_entrada);
    System.out.println(reservas[i].id_reserva);
   }



* */
  



    // restantes métodos...
}
