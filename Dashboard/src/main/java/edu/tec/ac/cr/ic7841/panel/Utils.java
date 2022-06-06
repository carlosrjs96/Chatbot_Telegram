package edu.tec.ac.cr.ic7841.panel;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.sql.*;
import java.util.Optional;

public class Utils {


    private static final String DBURL = "jdbc:sqlserver://localhost\\TestDB:1433;user=USUARIO;password=CLAVE";
    private static final String USUARIO = "USUARIO";
    private static final String CLAVE = "CLAVE";


    public static Optional<Connection> conectar() {
        try {
            Connection conn = DriverManager.getConnection(DBURL, USUARIO, CLAVE);
            return Optional.of(conn);

        } catch (SQLException e) {

            e.printStackTrace();
            return Optional.empty();

        }
    }

    public static Optional<ResultSet> consultar(PreparedStatement sql) {

        try {
            ResultSet resultado = sql.executeQuery();
            return Optional.of(resultado);

        } catch (SQLException e) {

            e.printStackTrace();
            return Optional.empty();

        }
    }

    public static void cargar(String escena, String titulo, Optional<ControladorPanel> cp) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Utils.class.getResource(escena));
        Parent root = fxmlLoader.load();
        Stage escenario = new Stage();
        if (escena.equals("editable-caracteristica.fxml")) {
            ControladorCaracteristica controlador = fxmlLoader.getController();
            controlador.setTipos();

        }
        if (cp.isPresent()) {
            Controlador controlador = fxmlLoader.getController();
            controlador.setControladorPanel(cp.get());
        }
        escenario.setResizable(false);
        escenario.setScene(new Scene(root));
        escenario.setTitle(titulo);
        escenario.show();
    }


    public static void ocultar(Scene escena) {
        escena.getWindow().hide();
    }

}
