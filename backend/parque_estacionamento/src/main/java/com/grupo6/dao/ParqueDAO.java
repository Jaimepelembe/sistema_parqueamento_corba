package com.grupo6.dao;

import com.grupo6.ParqueamentoApp.ParqueEstacionamento;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.List;

public class ParqueDAO {

    public List<ParqueEstacionamento> listar()
            throws SQLException {

        List<ParqueEstacionamento> parques =
                new ArrayList<>();

        String sql =
            "SELECT id_parque, nome, provincia, " +
            "localizacao, telefone, horario, " +
            "cobertura, preco, foto_url " +
            "FROM parque_estacionamento";

        try (
            Connection conn = ConexaoBD.conectar();
            PreparedStatement stmt =
                conn.prepareStatement(sql);
            ResultSet rs = stmt.executeQuery()
        ) {

            while (rs.next()) {

                ParqueEstacionamento parque =
                    new ParqueEstacionamento();

                parque.id_parque =
                    rs.getInt("id_parque");

                parque.nome =
                    rs.getString("nome");

                parque.provincia =
                    rs.getString("provincia");

                parque.localizacao =
                    rs.getString("localizacao");

                parque.telefone =
                    rs.getString("telefone");

                parque.horario =
                    rs.getString("horario");

                parque.precoHora =
                    rs.getDouble("preco");

                parque.fotoUrl =
                    rs.getString("foto_url");

                parques.add(parque);
            }
        }

        return parques;
    }
}