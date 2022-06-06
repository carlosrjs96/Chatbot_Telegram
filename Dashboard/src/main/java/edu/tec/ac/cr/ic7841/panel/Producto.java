package edu.tec.ac.cr.ic7841.panel;

public class Producto {

    private Integer id;
    private String nombre;

    public Producto(int id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    public Producto(String nombre) {
        this.nombre = nombre;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Producto{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' + '}';
    }

}
