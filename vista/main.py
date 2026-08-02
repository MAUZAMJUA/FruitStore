import os
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QVBoxLayout

from vista.frame_categoria import FrameCategoria
from vista.frame_producto import FrameProducto
from vista.frame_compra import FrameCompra
from vista.frame_proveedor import FrameProveedor
from vista.frame_vendedor import FrameVendedor
from vista.frame_venta import FrameVenta


base_path = os.path.dirname(__file__)
ui_path = os.path.join(base_path, "main.ui")

formulario_ui, clase_base = loadUiType(ui_path)  # type: ignore


class Main(clase_base, formulario_ui):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.frm_categoria = None
        self.frm_producto = None
        self.frm_compra = None
        self.frm_proveedor = None
        self.frm_vendedor = None
        self.frm_venta = None

        if self.frm_principal.layout() is None:
            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            self.frm_principal.setLayout(layout)

        self.__agregar_listeners()

    def __agregar_listeners(self):
        self.action_productos.triggered.connect(self.cargarModuloProductos)
        self.action_categorias.triggered.connect(self.cargarModuloCategorias)
        self.action_compras.triggered.connect(self.cargarModuloCompras)
        self.action_proveedores.triggered.connect(self.cargarModuloProveedores)
        self.action_vendedores.triggered.connect(self.cargarModuloVendedores)
        self.action_ventas.triggered.connect(self.cargarModuloVentas)

    def limpiar_contenedor_principal(self):
        layout = self.frm_principal.layout()

        if layout is None:
            return

        for i in range(layout.count()):
            item = layout.itemAt(i)

            if item is not None:
                widget = item.widget()

                if widget is not None:
                    widget.hide()

    def cargarModuloProductos(self):
        self.limpiar_contenedor_principal()

        if self.frm_producto is None:
            self.frm_producto = FrameProducto()
            self.frm_principal.layout().addWidget(self.frm_producto)
            print("Se agregó productos")

        self.frm_producto.show()

    def cargarModuloCategorias(self):
        self.limpiar_contenedor_principal()

        if self.frm_categoria is None:
            self.frm_categoria = FrameCategoria()
            self.frm_principal.layout().addWidget(self.frm_categoria)
            print("Se agregó categorías")

        self.frm_categoria.show()

    def cargarModuloCompras(self):
        self.limpiar_contenedor_principal()

        if self.frm_compra is None:
            self.frm_compra = FrameCompra()
            self.frm_principal.layout().addWidget(self.frm_compra)
            print("Se agregó compra")

        self.frm_compra.show()

    def cargarModuloProveedores(self):
        self.limpiar_contenedor_principal()

        if self.frm_proveedor is None:
            self.frm_proveedor = FrameProveedor()
            self.frm_principal.layout().addWidget(self.frm_proveedor)
            print("Se agregó proveedor")

        self.frm_proveedor.show()

    def cargarModuloVendedores(self):
        self.limpiar_contenedor_principal()

        if self.frm_vendedor is None:
            self.frm_vendedor = FrameVendedor()
            self.frm_principal.layout().addWidget(self.frm_vendedor)
            print("Se agregó vendedor")

        self.frm_vendedor.show()

    def cargarModuloVentas(self):
        self.limpiar_contenedor_principal()

        if self.frm_venta is None:
            self.frm_venta = FrameVenta()
            self.frm_principal.layout().addWidget(self.frm_venta)
            print("Se agregó venta")

        self.frm_venta.show()