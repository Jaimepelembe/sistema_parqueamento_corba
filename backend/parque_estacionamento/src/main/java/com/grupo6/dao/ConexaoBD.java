package com.grupo6.dao;


import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class ConexaoBD {
    // Caminho onde o arquivo do banco de dados será salvo
    // O modo WAL permite que leituras e escritas ocorram simultaneamente sem bloquear o banco de dados.
    // Define o tempo limite de espera para 5000ms (5 segundos) antes de lançar SQLITE_BUSY
    public static Connection conectar() {
        Connection conexao = null;
        //C:\Users\jaimi\OneDrive\Documentos\programacao\parque_estacionamento_corba\backend\base_dados\parqueamentoBD.db
        try {
            // Realiza a conexão com o banco de dados
            String URL = getUrlDatabase()+"?journal_mode=WAL";            //"jdbc:sqlite:backend/base_dados/parqueamentoBD.db?journal_mode=WAL"; 
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
    
    private static String getUrlDatabase() {
        // Pega a pasta de trabalho atual
        File pastaAtual = new File(System.getProperty("user.dir"));

        // Se o terminal estiver dentro de 'parque_estacionamento', sobe um nível para 'backend'
        if (pastaAtual.getName().equalsIgnoreCase("parque_estacionamento")) {
            pastaAtual = pastaAtual.getParentFile();
        }

        // Constrói o caminho exato apontando para backend/base_dados/parqueamentoBD.db
        File arquivoBD = new File(pastaAtual, "base_dados" + File.separator + "parqueamentoBD.db");

        // Garante que a pasta 'base_dados' é criada no disco caso ainda não exista
        if (!arquivoBD.getParentFile().exists()) {
            arquivoBD.getParentFile().mkdirs();
        }

        // Retorna o caminho absoluto convertido para a URL JDBC do SQLite
        return "jdbc:sqlite:" + arquivoBD.getAbsolutePath();
    }

    public static void main(String[] args) {
        ConexaoBD.conectar();
        //System.out.println(getUrlDatabase());
    }
}
