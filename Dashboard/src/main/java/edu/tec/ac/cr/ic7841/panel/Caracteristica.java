package edu.tec.ac.cr.ic7841.panel;

import java.math.BigDecimal;

public class Caracteristica {


    private Integer id;
    private Integer idProducto;
    private BigDecimal precio;
    private String nombre;
    private String tipo;

    public Caracteristica(Integer id, Integer idProducto, BigDecimal precio, String nombre, String tipo) {
        this.id = id;
        this.idProducto = idProducto;
        this.precio = precio;
        this.nombre = nombre;
        this.tipo = tipo;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getIdProducto() {
        return idProducto;
    }

    public void setIdProducto(Integer idProducto) {
        this.idProducto = idProducto;
    }

    public BigDecimal getPrecio() {
        return precio;
    }

    public void setPrecio(BigDecimal precio) {
        this.precio = precio;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    @Override
    public String toString() {
        return "Caracteristica{" +
                "id=" + id +
                ", idProducto=" + idProducto +
                ", precio=" + precio +
                ", nombre='" + nombre + '\'' +
                ", tipo='" + tipo + '\'' +
                '}';
    }
}
