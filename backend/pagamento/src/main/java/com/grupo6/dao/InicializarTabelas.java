package com.grupo6.dao;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;



public class InicializarTabelas{

    public static void main(String[] args) {
        try{
    Connection conn = ConexaoBD.conectar();
    criarTabelas(conn);
    inserirDadosExemplo(conn);

     if (!conn.isClosed()) {
        conn.close();
        System.out.println("Conexão com SQLite fechada com sucesso!");
                    }
    }catch (Exception e) {
            System.err.println("Erro: " + e.getMessage());
        }
}

public static void criarTabelas(Connection conn){
        try{
        
        if (conn != null){
            
        Statement stmt = conn.createStatement();

        String sql="";

                  //Criar tabela  conta

        sql= "CREATE TABLE IF NOT EXISTS conta (id_conta INTEGER PRIMARY KEY AUTOINCREMENT,  "
                +"saldo REAL NOT NULL DEFAULT 0,  "
                +"id_usuario INTEGER NOT NULL UNIQUE);";

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





    }
    } 
    catch (SQLException e){

    System.err.println("Erro ao criar as tabelas conta ou transacao : " + e.getMessage());
}
    
    catch (Exception e){
    System.err.println("Erro: " + e.getMessage());
    }

}


public static void inserirDadosExemplo(Connection conn){

    try{
        String[] inserts = {
            "INSERT INTO conta(saldo, id_usuario) VALUES (1500.00, 1), (500.00, 2), (250.50, 3);",
            "INSERT INTO transacao(tipo, valor, estado, data, hora, id_conta) VALUES ('DEPOSITO', 2000.0, 'CONCLUIDO', '2026-09-26', '14:30', 1), ('PAGAMENTO_RESERVA', 200.0, 'CONCLUIDO', '2026-09-27', '08:05', 1), ('DEPOSITO', 500.0, 'CONCLUIDO', '2026-09-27', '09:15', 2);"
       
        };

 



        String[] selectSql={
            "SELECT EXISTS (SELECT 1 FROM conta) AS resultado;",
            "SELECT EXISTS (SELECT 1 FROM transacao) AS resultado;"
        };


    Statement stmt = conn.createStatement();

    //for (String insertSql : inserts) {
      
    for (int i=0; i<inserts.length;i++){
        //Verificar se ja existe algum registo em cada tabela da base de dados
        String selectQuery= selectSql[i];
        ResultSet  rs= stmt.executeQuery(selectQuery);
        if(rs.next()){
            boolean possuiRegisto= rs.getBoolean("resultado");
            if (!possuiRegisto){
                stmt.executeUpdate(inserts[i]);
                System.out.println(" Nao possui nem um registo");
                
            }
     

        }
        

    }
    System.out.println("Dados de teste inseridos com sucesso!");
   
}
    catch (SQLException e){

    System.err.println("Erro ao inserir dados de exemplo: " + e.getMessage());
}
    
    catch (Exception e){
    System.err.println("Erro: " + e.getMessage());
    }



}



}

