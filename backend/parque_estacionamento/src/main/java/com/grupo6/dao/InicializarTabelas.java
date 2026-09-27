package com.grupo6.dao;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.SQLException;
//import com.grupo6.dao.ConexaoBD;


public class InicializarTabelas{

    public static void main(String[] args) {
        try{
        Connection conn = ConexaoBD.conectar();
        if (conn != null){
             String sql = "CREATE TABLE IF NOT EXISTS usuario ( " +
             "id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, " +
             "nome TEXT NOT NULL, " +
             "telefone TEXT NOT NULL UNIQUE, " +
             "senha TEXT NOT NULL, " +
             "tipo INTEGER NOT NULL DEFAULT 0" +
             ");";
            
            Statement stmt = conn.createStatement();
            stmt.execute(sql);

    

            //Criar tabela parque_estacionamento
            sql= "CREATE TABLE IF NOT EXISTS parque_estacionamento (id_parque INTEGER PRIMARY KEY AUTOINCREMENT, "
            + "nome TEXT NOT NULL, "
            + "provincia TEXT NOT NULL, "
            + "localizacao TEXT NOT NULL, "
            + "telefone TEXT, "
            + "horario TEXT, "
            + "cobertura TEXT, "
            + "preco REAL NOT NULL, "
            + "foto_url TEXT);";
            stmt.execute(sql);
        
   
        //Criar tabela viatura

        sql ="CREATE TABLE IF NOT EXISTS viatura (id_viatura INTEGER PRIMARY KEY AUTOINCREMENT, "
            +"marca TEXT NOT NULL, "
            +"modelo TEXT NOT NULL, "
            +"matricula TEXT NOT NULL UNIQUE, "
           + "id_usuario INTEGER NOT NULL, "

           +" FOREIGN KEY (id_usuario) "
                +"REFERENCES usuario(id_usuario) "
                +"ON DELETE CASCADE "
                +"ON UPDATE CASCADE );";
        
        stmt.execute(sql);


        //Criar tabela  conta

        sql= "CREATE TABLE IF NOT EXISTS conta (id_conta INTEGER PRIMARY KEY AUTOINCREMENT,  "
                +"saldo REAL NOT NULL DEFAULT 0,  "
                +"id_usuario INTEGER NOT NULL UNIQUE,  "

                +"FOREIGN KEY (id_usuario)  "
                    +"REFERENCES usuario(id_usuario)  "
                    +"ON DELETE CASCADE  "
                    +"ON UPDATE CASCADE);";

            stmt.execute(sql);

            //Criar tabela vaga_estacionamento

            sql = "CREATE TABLE IF NOT EXISTS vaga_estacionamento (id_vaga INTEGER PRIMARY KEY AUTOINCREMENT, "
            +"numero_vaga TEXT NOT NULL, "
            +"estado INTEGER NOT NULL DEFAULT 0, "
            +"id_parque INTEGER NOT NULL, "
           + "id_usuario INTEGER, "

            +"FOREIGN KEY (id_parque) "
                +"REFERENCES parque_estacionamento(id_parque) "
                +"ON DELETE CASCADE "
               + "ON UPDATE CASCADE, "

            +"FOREIGN KEY (id_usuario) "
                +"REFERENCES usuario(id_usuario) "
                +"ON DELETE SET NULL "
                +"ON UPDATE CASCADE);";
        stmt.execute(sql);

        //Criar tabela reserva_vaga
        sql = "CREATE TABLE IF NOT EXISTS reserva_vaga (id_reserva INTEGER PRIMARY KEY AUTOINCREMENT, "

           +" data_entrada TEXT NOT NULL, "
            +"hora_entrada TEXT NOT NULL, "

           +"data_saida TEXT NOT NULL, "
           +"hora_saida TEXT NOT NULL, "

            +"preco_total REAL NOT NULL, "

           + "id_vaga INTEGER NOT NULL, "
            +"id_usuario INTEGER NOT NULL, "
            +"id_viatura INTEGER NOT NULL, "

           + "FOREIGN KEY (id_vaga) "
               + "REFERENCES vaga_estacionamento(id_vaga) "
                +"ON DELETE RESTRICT "
                +"ON UPDATE CASCADE, "

            +"FOREIGN KEY (id_usuario) "
                +"REFERENCES usuario(id_usuario) "
                +"ON DELETE RESTRICT "
                +"ON UPDATE CASCADE, "

            +"FOREIGN KEY (id_viatura) "
                +"REFERENCES viatura(id_viatura) "
                +"ON DELETE RESTRICT "
                +"ON UPDATE CASCADE);";
        stmt.execute(sql);

  
        //Criar tabela  transacao
        sql = "CREATE TABLE IF NOT EXISTS transacao (id_transacao INTEGER PRIMARY KEY AUTOINCREMENT, "
            +"tipo TEXT NOT NULL, "
            +"valor REAL NOT NULL, "
            +"estado TEXT NOT NULL, "
           +"data TEXT NOT NULL, "
           + "hora TEXT NOT NULL, "

            +"id_conta INTEGER NOT NULL, "

            +"FOREIGN KEY (id_conta) "
                +"REFERENCES conta(id_conta) "
                +"ON DELETE RESTRICT "
                +"ON UPDATE CASCADE);";
        stmt.execute(sql);
      /**
* */


        }
    } 
    catch (SQLException e){

    System.err.println("Erro ao criar a tabela usuario: " + e.getMessage());
}
    
    catch (Exception e){
    System.err.println("Erro: " + e.getMessage());
    }

}

public static void inserirDadosExemplo(){

    


}



}

