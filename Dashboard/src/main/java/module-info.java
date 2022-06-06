module edu.tec.ac.cr.ic7841.paneladministrador {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;
    requires java.sql;

    exports edu.tec.ac.cr.ic7841.panel;
    opens edu.tec.ac.cr.ic7841.panel to javafx.fxml;
}