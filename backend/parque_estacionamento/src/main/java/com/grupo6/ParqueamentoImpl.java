package com.grupo6;
import com.grupo6.dao.ParqueDAO;
import com.grupo6.dao.InicializarTabelas;

import com.grupo6.ParqueamentoApp.*;

import java.sql.SQLException;
import java.util.List;

public class ParqueamentoImpl
        extends SistemaParqueamentoPOA {
    
    private ParqueDAO parqueDAO;


    public ParqueamentoImpl() {

        
    }

    @Override
    public Usuario login(
            String telefone,
            String senha)
            throws UsuarioNaoEncontrado {

        return null;
    }

    @Override
    public ParqueEstacionamento[] listarParques() {
        
        try {
            parqueDAO = new ParqueDAO();
            List<ParqueEstacionamento> lista =
                    parqueDAO.listar();

            return lista.toArray(
                    new ParqueEstacionamento[0]
            );

        } catch (SQLException e) {

            e.printStackTrace();

            return new ParqueEstacionamento[0];
        }
    }

    @Override
    public ParqueEstacionamento[] pesquisarPorProvincia(
            String provincia) {

        return null;
    }

    @Override
    public ParqueEstacionamento[] pesquisarPorNome(
            String nome) {

        return null;
    }

    @Override
    public ParqueEstacionamento[] pesquisarPorPreco(
            double precoMaximo) {

        return null;
    }

    @Override
    public void adicionarParque(
            ParqueEstacionamento parque)
            throws OperacaoInvalida {

    }

    @Override
    public void editarParque(
            ParqueEstacionamento parque)
            throws ParqueNaoEncontrado, OperacaoInvalida {

    }

    @Override
    public void removerParque(
            int id_parque)
            throws ParqueNaoEncontrado {

    }

    public static void main(String[] args){
        //Inicializar as tabelas caso elas nao existam

    }

    // restantes métodos...
}