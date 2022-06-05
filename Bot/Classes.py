import enum
#----------------------------------------------------------------
class Flujo:
    # Constructor
    def __init__(self):
        self.producto         : Producto  = Producto()
        self.cliente          : Cliente   = Cliente()
        self.preguntas        : list[str] = []
        self.numero_pregunta  : int       = 0
#----------------------------------------------------------------
class Producto:
    def __init__(self):
        self.nombre          : str  = ""
        self.caracteristicas : list[Caracteristica] = []
    def get_Total(self)->int:
        total = 0
        for caracteristica in self.caracteristicas:
            total += caracteristica.precio
        return total
#----------------------------------------------------------------
class Caracteristica:
    def __init__(self):
        self.nombre : str  = ""
        self.tipo   : Tipo_Caracteristica = None
        self.precio : float = 0
#----------------------------------------------------------------
class Tipo_Caracteristica(enum.Enum):
    TAMANO        = 0
    EXTRAPERSONA  = 1
    EXTRAMASCOTA  = 2
    FONDO         = 3
    MOTAJE        = 4
#----------------------------------------------------------------
class Cliente:
    def __init__(self):
        self.nombre         : str = ""
        self.user_Telegram  : str = ""
        self.user_Instagram : str = ""      
        self.celular        : str = ""