package edu.tec.ac.cr.ic7841.panel;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.VBox;

import java.io.IOException;
import java.net.URL;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Optional;
import java.util.ResourceBundle;

public class ControladorPanel implements Initializable {


    private Connection conexion;

    private int ultimaCaracteristica = 0;

    private int ultimoProducto = 0;

    public int idSeleccionado = 0;

    @FXML
    private Button btnSalir;

    @FXML
    private Button btnOrdenes;

    @FXML
    private Button btnPanel;


    @FXML
    private Button btnAgregarCaracteristica;

    @FXML
    private Button btnAgregarProducto;

    @FXML
    private TextField editableTipo;

    @FXML
    private VBox panelProductos = null;

    @FXML
    private VBox panelCaracteristicas = null;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        configurar();
        mostrarTablaProductos();
    }

    public void configurar() {
        Optional<Connection> conexion = Utils.conectar();
        conexion.ifPresent(connection -> this.conexion = connection);
    }


    public ArrayList<Producto> obtenerProductos() {

        ArrayList<Producto> encontrados = new ArrayList<>();
        Producto producto;

        try {

            PreparedStatement sql = conexion.prepareStatement("SELECT * FROM Producto");
            Optional<ResultSet> productos = Utils.consultar(sql);

            if (productos.isPresent()) {

                ResultSet resultado = productos.get();

                while (resultado.next()) {
                    producto = new Producto(resultado.getInt("id"),
                            resultado.getString("nombre"));
                    encontrados.add(producto);
                }
            }

        } catch (SQLException sqle) {

            sqle.printStackTrace();
            encontrados = new ArrayList<>();
        }
        return encontrados;
    }

    public void mostrarTablaProductos() {
        panelProductos.getChildren().remove(0, ultimoProducto);
        ArrayList<Producto> productos = obtenerProductos();
        ultimoProducto = productos.size();
        for (Producto producto : productos) {
            try {
                FXMLLoader loader = new FXMLLoader(getClass().getResource("producto.fxml"));
                Node nodo = loader.load();
                ControladorProducto controladorProducto = loader.getController();
                controladorProducto.setProducto(producto);
                controladorProducto.setControladorPanel(this);
                controladorProducto.setTextos();
                panelProductos.getChildren().add(nodo);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }

    public ObservableList<Caracteristica> obtenerCaracteristicas() {

        ObservableList<Caracteristica> encontrados = FXCollections.observableArrayList();
        Caracteristica caracteristica;

        try {

            PreparedStatement caracteristicas = conexion.prepareStatement("SELECT * FROM Caracteristica WHERE id_producto = ?");
            caracteristicas.setInt(1, idSeleccionado);
            Optional<ResultSet> consultado = Utils.consultar(caracteristicas);

            if (consultado.isPresent()) {

                ResultSet resultado = consultado.get();

                while (resultado.next()) {
                    caracteristica = new Caracteristica(
                            resultado.getInt("id"),
                            resultado.getInt("id_producto"),
                            resultado.getBigDecimal("precio"),
                            resultado.getString("nombre"),
                            resultado.getString("tipo"));
                    encontrados.add(caracteristica);
                }
            }

        } catch (SQLException sqle) {

            sqle.printStackTrace();
            encontrados = FXCollections.emptyObservableList();
        }
        return encontrados;
    }


    private void mostrarTablaCaracteristicas() {
        panelCaracteristicas.getChildren().remove(0, ultimaCaracteristica);
        ObservableList<Caracteristica> caracteristicas = obtenerCaracteristicas();
        ultimaCaracteristica = caracteristicas.size();
        for (Caracteristica caracteristica : caracteristicas) {
            try {
                FXMLLoader loader = new FXMLLoader(getClass().getResource("caracteristica.fxml"));
                Node nodo = loader.load();
                ControladorCaracteristica controladorCaracteristica = loader.getController();
                controladorCaracteristica.setCaracteristica(caracteristica);
                controladorCaracteristica.setControladorPanel(this);
                controladorCaracteristica.setTextos();
                panelCaracteristicas.getChildren().add(nodo);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }

    protected void seleccionar(int idProducto) {
        idSeleccionado = idProducto;
        System.out.println("SELECCCIONADO ES: " + idProducto);
        mostrarTablaCaracteristicas();
    }

    protected void eliminar(Caracteristica caracteristica) {
        try {
            PreparedStatement eliminado = conexion.prepareStatement("DELETE FROM Caracteristica WHERE id = (?)");
            eliminado.setInt(1, caracteristica.getId());
            eliminado.executeUpdate();
            mostrarTablaCaracteristicas();
        } catch (SQLException sqle) {
            sqle.printStackTrace();
        }
    }

    protected void eliminar(Producto producto) {
        try {
            PreparedStatement eliminado = conexion.prepareStatement("DELETE FROM Producto WHERE id = (?)");
            eliminado.setInt(1, producto.getId());
            eliminado.executeUpdate();
            mostrarTablaProductos();
        } catch (SQLException sqle) {
            sqle.printStackTrace();
        }
    }


    @FXML
    public void salir(MouseEvent event) throws SQLException {
        conexion.close();
        System.exit(0);
    }

    @FXML
    protected void cargarNuevoProducto() throws IOException {
        Utils.cargar("editable-producto.fxml", "Editar producto", Optional.of(this));
    }

    @FXML
    protected void cargarNuevaCaracteristica() throws IOException {
        Utils.cargar("editable-caracteristica.fxml", "Editar caracteristica", Optional.of(this));

    }


    protected void actualizar(Producto producto) throws SQLException {
        PreparedStatement actualizado = conexion.prepareStatement("UPDATE Producto SET nombre = ? WHERE id = ?");
        actualizado.setString(1,  producto.getNombre());
        actualizado.setInt(2, producto.getId());
        actualizado.executeUpdate();
        mostrarTablaProductos();
    }

    protected void insertar(Producto producto) throws SQLException {
        PreparedStatement insertado = conexion.prepareStatement("INSERT INTO Producto VALUES (?)");
        insertado.setString(1,  producto.getNombre());
        insertado.executeUpdate();
        mostrarTablaProductos();

    }


    protected void insertar(Caracteristica caracteristica) throws SQLException {
        PreparedStatement insertado = conexion.prepareStatement("INSERT INTO Caracteristica VALUES (?, ?, ?, ?)");
        insertado.setInt(1, caracteristica.getIdProducto());
        insertado.setString(2, caracteristica.getNombre());
        insertado.setString(3, caracteristica.getTipo());
        insertado.setBigDecimal(4, caracteristica.getPrecio());
        insertado.executeUpdate();
        mostrarTablaCaracteristicas();
    }


    protected void actualizar(Caracteristica caracteristica) throws SQLException {
        PreparedStatement actualizado = conexion.prepareStatement("UPDATE Caracteristica SET nombre = ?, tipo = ?, precio = ? WHERE id = ?");
        actualizado.setString(1,  caracteristica.getNombre());
        actualizado.setString(2,  caracteristica.getTipo());
        actualizado.setBigDecimal(3, caracteristica.getPrecio());
        actualizado.setInt(4, caracteristica.getId());
        actualizado.executeUpdate();
        mostrarTablaCaracteristicas();
    }

}
