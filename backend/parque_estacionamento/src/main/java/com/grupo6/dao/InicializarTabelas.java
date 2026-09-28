package com.grupo6.dao;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;
//import com.grupo6.dao.ConexaoBD;


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

            +"FOREIGN KEY (id_parque) "
                +"REFERENCES parque_estacionamento(id_parque) "
                +"ON DELETE CASCADE "
               + "ON UPDATE CASCADE );";
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

        }
    } 
    catch (SQLException e){

    System.err.println("Erro ao criar as tabelas : " + e.getMessage());
}
    
    catch (Exception e){
    System.err.println("Erro: " + e.getMessage());
    }

}


public static void inserirDadosExemplo(Connection conn){

    try{
        String[] inserts = {
        "INSERT INTO usuario (nome, telefone, senha, tipo) VALUES ('Carlos Mucavele', '841234567', 'senha123', 1), ('Anabela Sitoe', '829876543', 'senha123', 0), ('Mateus Langa', '855554433', 'senha123', 0);",
        
        "INSERT INTO parque_estacionamento (nome, provincia, localizacao, telefone, horario, cobertura, preco, foto_url) VALUES ('Parque Central', 'Maputo', 'Av. 25 de Setembro', '840001122', '07:00-22:00', 'COBERTO', 50.0, 'https://fotos.com/p1.jpg'), ('Parque Matola Plaza', 'Maputo', 'Av. das Indústrias', '820003344', '08:00-20:00', 'NAO_COBERTO', 30.0, 'https://fotos.com/p2.jpg'), ('Parque Beira Mar', 'Sofala', 'Av. das Mambas', '850005566', '24 Horas', 'COBERTO', 40.0, 'https://fotos.com/p3.jpg');",
        
        "INSERT INTO viatura (marca, modelo, matricula, id_usuario) VALUES ('Toyota', 'Corolla', 'ABC-123-MC', 1), ('Nissan', 'Hardbody', 'AFG-456-MC', 2), ('Hyundai', 'Elantra', 'AIA-789-MC', 3);",
    
        "INSERT INTO vaga_estacionamento (numero_vaga, estado, id_parque) VALUES ('A-01', 1, 1), ('A-02', 0, 2), ('A-01', 0, 3);",
        
        "INSERT INTO reserva_vaga (data_entrada, hora_entrada, data_saida, hora_saida, preco_total, id_vaga, id_usuario, id_viatura) VALUES ('2026-09-27', '08:00', '2026-09-27', '12:00', 200.0, 1, 1, 1), ('2026-09-28', '10:00', '2026-09-28', '14:00', 120.0, 3, 2, 2), ('2026-09-29', '14:00', '2026-09-29', '18:00', 160.0, 2, 3, 3);",
        
        };

        //Tabelas da base de dados Transacao
        // "INSERT INTO conta (saldo, id_usuario) VALUES (1500.00, 1), (500.00, 2), (250.50, 3);",
        // "INSERT INTO transacao (tipo, valor, estado, data, hora, id_conta) VALUES ('DEPOSITO', 2000.0, 'CONCLUIDO', '2026-09-26', '14:30', 1), ('PAGAMENTO_RESERVA', 200.0, 'CONCLUIDO', '2026-09-27', '08:05', 1), ('DEPOSITO', 500.0, 'CONCLUIDO', '2026-09-27', '09:15', 2);"
       



        String[] selectSql={
            "SELECT EXISTS (SELECT 1 FROM usuario) AS resultado;",
            "SELECT EXISTS (SELECT 1 FROM parque_estacionamento) AS resultado;",
            "SELECT EXISTS (SELECT 1 FROM viatura) AS resultado;",
            "SELECT EXISTS (SELECT 1 FROM vaga_estacionamento) AS resultado;",
            "SELECT EXISTS (SELECT 1 FROM reserva_vaga) AS resultado;"
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

