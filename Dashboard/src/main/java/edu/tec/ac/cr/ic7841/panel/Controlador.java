package edu.tec.ac.cr.ic7841.panel;

import javafx.scene.input.MouseEvent;

import java.io.IOException;

public interface Controlador {

    void cargar(MouseEvent mouseEvent) throws IOException;

    void setControladorPanel(ControladorPanel cp);
}
