package edu.tec.ac.cr.ic7841.panel;

import javafx.application.Application;
import javafx.stage.Stage;

import java.util.Optional;

public class PanelAdministrador extends Application {

    public static void main(String[] args) {
        launch();
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        Utils.cargar("panel.fxml","Panel administrador", Optional.empty());
    }
}