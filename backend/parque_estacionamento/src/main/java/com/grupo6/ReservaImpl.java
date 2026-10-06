package com.grupo6;

import com.grupo6.ParqueamentoApp.ReservaPOA;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.Duration;

import com.grupo6.ParqueamentoApp.ReservaDTO;
import com.grupo6.dao.ReservaDAO;


public class ReservaImpl
        extends ReservaPOA {
    
    private ReservaDAO reservaDAO;


    public ReservaImpl() {

        
    }


    @Override
    public boolean criarReserva(ReservaDTO reserva){
        reservaDAO = new ReservaDAO();

        //float precoHoraParque=reservaDAO.obterPrecoHoraParque(reserva.id_vaga);
        //long tempoTotal=calcularTempoReserva(reserva.data_entrada, reserva.hora_entrada, reserva.data_saida, reserva.hora_saida);
        //float precoApagar=tempoTotal*precoHoraParque;

        //reserva.preco_total=precoApagar;
        //System.out.println("Preco vou pagar"+reserva.preco_total);
        
       return  reservaDAO.criarReserva(reserva);
    }



        @Override
    public ReservaDTO[] listarReservas(int id_usuario) {
         reservaDAO = new ReservaDAO();
        
        ReservaDTO[] listaReservas=  reservaDAO.listarReservas(id_usuario);

        return listaReservas;}
    

    @Override
    public ReservaDTO obterReserva(int id_reserva) {
         reservaDAO = new ReservaDAO();
        
        ReservaDTO reserva=  reservaDAO.obterReserva(id_reserva);

        return reserva;}

    
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
