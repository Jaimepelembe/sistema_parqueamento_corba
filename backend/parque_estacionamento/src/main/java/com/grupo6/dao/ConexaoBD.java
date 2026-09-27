package com.grupo6.dao;



import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class ConexaoBD {
    // Caminho onde o arquivo do banco de dados será salvo
    private static final String URL = "jdbc:sqlite:backend/base_dados/parqueamentoBD.db";

    public static Connection conectar() {
        Connection conexao = null;
        try {
            // Realiza a conexão com o banco de dados
            conexao = DriverManager.getConnection(URL);

            // Garante que as foreign keys são respeitadas (SQLite vem desativado por defeito)
            Statement stmt = conexao.createStatement();
            stmt.execute("PRAGMA foreign_keys = ON;");
            System.out.println("Conexão com SQLite realizada com sucesso!");
            
        } catch (SQLException e) {
            System.out.println("Erro ao conectar com o SQLite: " + e.getMessage());
        }
        return conexao;
    }
}
