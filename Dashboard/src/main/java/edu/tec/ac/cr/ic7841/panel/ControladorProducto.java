package edu.tec.ac.cr.ic7841.panel;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

import java.io.IOException;
import java.sql.SQLException;


public class ControladorProducto implements Controlador{

    private ControladorPanel controladorPanel;

    private Producto producto;

    @FXML
    private Button btnEliminar;

    @FXML
    private Button btnModificar;

    @FXML
    private Button btnCancelar;

    @FXML
    private Button btnGuardar;

    @FXML
    private HBox articuloProducto;

    @FXML
    private Label textoNombre;

    @FXML
    private Label textoNumero;


    @FXML
    private TextField editableNombre;



    public void setControladorPanel(ControladorPanel controladorPanel) {
        this.controladorPanel = controladorPanel;
    }

    protected void setProducto(Producto producto) {
        this.producto = producto;
    }

    protected void setTextos() {
        textoNombre.setText(producto.getNombre());
        textoNumero.setText(Integer.toString(producto.getId()));
    }

    protected void setEditables(Producto producto) {
        editableNombre.setText(producto.getNombre());
    }


    @FXML
    private void oscurecer() {
        articuloProducto.setStyle("-fx-background-color : #f3f3f3");
    }

    @FXML
    private void aclarar() {
        articuloProducto.setStyle("-fx-background-color : #ffffff");
    }

    @FXML
    private void seleccionar() {
        controladorPanel.seleccionar(producto.getId());
    }

    @FXML
    private void eliminar(MouseEvent event) {
        controladorPanel.eliminar(producto);
    }

    @FXML
    public void cargar(MouseEvent event) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("editable-producto.fxml"));
        Parent root = fxmlLoader.load();
        Stage nuevo = new Stage();
        ControladorProducto controlador = fxmlLoader.getController();
        controlador.setEditables(producto);
        controlador.setProducto(producto);
        controlador.setControladorPanel(controladorPanel);
        controlador.btnGuardar.setOnMouseClicked(actualizar(controlador, event));
        nuevo.setTitle("Editar producto");
        nuevo.setResizable(false);
        nuevo.setScene(new Scene(root));
        nuevo.show();

    }

    @FXML
    private void insertar(MouseEvent mouseEvent) throws SQLException {
        Producto nuevoProducto = new Producto(editableNombre.getText());
        controladorPanel.insertar(nuevoProducto);
        Scene escenaActual = ((Node) (mouseEvent.getSource())).getScene();
        Utils.ocultar(escenaActual);
    }

    private EventHandler<MouseEvent> actualizar(ControladorProducto controlador, MouseEvent mouseEvent){
        return event -> {
            try {
                Producto nuevoProducto = new Producto(producto.getId(),
                        controlador.editableNombre.getText());
                controladorPanel.actualizar(nuevoProducto);
                Scene escenaActual = controlador.editableNombre.getScene();
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
