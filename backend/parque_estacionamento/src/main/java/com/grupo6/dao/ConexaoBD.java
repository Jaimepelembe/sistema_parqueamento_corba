package com.grupo6.dao;



import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class ConexaoBD {
    // Caminho onde o arquivo do banco de dados será salvo
    // O modo WAL permite que leituras e escritas ocorram simultaneamente sem bloquear o banco de dados.
    // Define o tempo limite de espera para 5000ms (5 segundos) antes de lançar SQLITE_BUSY
    private static final String URL = "jdbc:sqlite:backend/base_dados/parqueamentoBD.db?journal_mode=WAL"; 

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

    public static void main(String[] args) {
        ConexaoBD.conectar();
    }
}
