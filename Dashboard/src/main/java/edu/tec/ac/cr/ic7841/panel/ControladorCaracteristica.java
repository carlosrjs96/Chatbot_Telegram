package edu.tec.ac.cr.ic7841.panel;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

import java.io.IOException;
import java.math.BigDecimal;
import java.sql.SQLException;

public class ControladorCaracteristica implements Controlador {

    private Caracteristica caracteristica;

    private ControladorPanel controladorPanel;

    @FXML
    private HBox articuloCaracteristica;

    @FXML
    private Button btnEliminar;

    @FXML
    private Button btnModificar;

    @FXML
    private Button btnCancelar;

    @FXML
    private Button btnGuardar;

    @FXML
    private Label textoNombre;

    @FXML
    private Label textoNumero;

    @FXML
    private Label textoPrecio;

    @FXML
    private Label textoTipo;

    @FXML
    private TextField editableNombre;

    @FXML
    private TextField editablePrecio;

    @FXML
    private ComboBox<String> editableTipo;


    public void setControladorPanel(ControladorPanel controladorPanel) {
        this.controladorPanel = controladorPanel;
    }

    protected void setCaracteristica(Caracteristica caracteristica) {
        this.caracteristica = caracteristica;
    }


    protected void setTextos() {
        textoNombre.setText(caracteristica.getNombre());
        textoNumero.setText(Integer.toString(caracteristica.getId()));
        textoPrecio.setText("₡ " + caracteristica.getPrecio());
        textoTipo.setText(caracteristica.getTipo());

    }

    protected void setEditables(Caracteristica caracteristica) {
        editableNombre.setText(caracteristica.getNombre());
        editablePrecio.setText(caracteristica.getPrecio().toString());
        editableTipo.setValue(caracteristica.getTipo());
        editableTipo.setPromptText(caracteristica.getTipo());
        setTipos();
    }

    protected void setTipos() {
        ObservableList<String> tipos =
                FXCollections.observableArrayList(
                        "TAMANO",
                        "FONDO",
                        "EXTRAMASCOTA",
                        "EXTRAPERSONA",
                        "MOTAJE"
                );
        editableTipo.setItems(tipos);
    }

    @FXML
    void aclarar(MouseEvent event) {
        articuloCaracteristica.setStyle("-fx-background-color : #ffffff");
    }

    @FXML
    void oscurecer(MouseEvent event) {
        articuloCaracteristica.setStyle("-fx-background-color : #f3f3f3");
    }

    @FXML
    void seleccionar(MouseEvent event) {
    }

    @FXML
    private void eliminar(MouseEvent event) {
        controladorPanel.eliminar(caracteristica);
    }


    @FXML
    public void cargar(MouseEvent event) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("editable-caracteristica.fxml"));
        Parent root = fxmlLoader.load();
        Stage nuevo = new Stage();
        ControladorCaracteristica controlador = fxmlLoader.getController();
        controlador.setEditables(caracteristica);
        controlador.setCaracteristica(caracteristica);
        controlador.setControladorPanel(controladorPanel);
        controlador.btnGuardar.setOnMouseClicked(actualizar(controlador, event));
        nuevo.setTitle("Editar caracteristica");
        nuevo.setResizable(false);
        nuevo.setScene(new Scene(root));
        nuevo.show();
    }

    @FXML
    private void insertar(MouseEvent mouseEvent) throws SQLException {
        Caracteristica nuevaCaracteristica = new Caracteristica(1,
                controladorPanel.idSeleccionado,
                new BigDecimal(editablePrecio.getText()),
                editableNombre.getText(),
                editableTipo.getValue());
        controladorPanel.insertar(nuevaCaracteristica);
        Scene escenaActual = ((Node) (mouseEvent.getSource())).getScene();
        Utils.ocultar(escenaActual);

    }

    private EventHandler<MouseEvent> actualizar(ControladorCaracteristica controlador, MouseEvent mouseEvent) {
        return event -> {
            try {
                Caracteristica nuevaCaracteristica = new Caracteristica(caracteristica.getId(),
                        caracteristica.getIdProducto(),
                        new BigDecimal((controlador.editablePrecio.getText())),
                        controlador.editableNombre.getText(),
                        controlador.editableTipo.getValue());
                controladorPanel.actualizar(nuevaCaracteristica);
                Scene escenaActual = controlador.editablePrecio.getScene();
                Utils.ocultar(escenaActual);
            } catch (SQLException sqle) {
                sqle.printStackTrace();
            }
        };
    }

    @FXML
    private void cancelar(MouseEvent mouseEvent) {
        Scene escenaActual = ((Node) (mouseEvent.getSource())).getScene();
        Utils.ocultar(escenaActual);
    }


}
