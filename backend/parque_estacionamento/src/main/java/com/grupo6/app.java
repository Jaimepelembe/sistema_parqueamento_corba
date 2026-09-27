package com.grupo6;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import com.grupo6.dao.ConexaoBD;

import java.sql.SQLException;

public class app {
    public static void main(String[] args) {
        try{
        Connection conn = ConexaoBD.conectar();
        if (conn != null){
              String sql = "CREATE TABLE IF NOT EXISTS vagas ( "+
               " id INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "numero TEXT NOT NULL UNIQUE,"+
                "ocupada INTEGER NOT NULL DEFAULT 0"+
           " );";
            
            Statement stmt = conn.createStatement();
            stmt.execute(sql.trim());
           
           //Inserir uma vaga
            String sql2 = "INSERT INTO vagas(numero) VALUES(?)";

            PreparedStatement pstmt = conn.prepareStatement(sql2);
            pstmt.setString(1, "20");
            pstmt.executeUpdate();

            String sql3 ="select numero from vagas";
            ResultSet resultado =stmt.executeQuery(sql3.trim());
            List<String> vagas = new ArrayList<>();
            while (resultado.next()){
                vagas.add(resultado.getString("numero"));
            }
            System.err.println(vagas.get(0));


            System.out.print("Connectado com sucesso");
        }
}
catch (SQLException e){

    System.err.println("Erro ao criar vaga: " + e.getMessage());
}


    }
    
}
