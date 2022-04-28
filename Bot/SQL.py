# Import Libraries
import pyodbc
import Classes
import Util
#region General Functions

#-----------------------------------------------------------------------
class DBConnector(object):
    
    def __init__(self):
        _json = Util.load_Json('Config.json')
        self.driver   = _json['driver']
        self.server   = _json['server']
        self.database = _json['database']
        self.user     = _json['user']
        self.password = _json['password']
        self.dbconn   = None

    # Create new connection
    def create_connection(self):
        return pyodbc.connect("DRIVER={};".format(self.driver) + \
                              "SERVER={};".format(self.server) + \
                              "DATABASE={};".format(self.database) + \
                              "UID={};".format(self.user) + \
                              "PWD={};".format(self.password) + \
                              "Trusted_Connection=yes;" + \
                              "CHARSET=UTF8",
                              ansi=True)

    # For explicitly opening database connection
    def __enter__(self):
        self.dbconn = self.create_connection()
        return self.dbconn

    def __exit__(self):
        self.dbconn.close()
#-----------------------------------------------------------------------
class DBConnection(object):
    connection = None

    @classmethod
    def get_connection(cls, new=False):
        """Creates return new Singleton database connection"""
        if new or not cls.connection:
            cls.connection = DBConnector().create_connection()
        return cls.connection

    @classmethod
    def execute_query(cls, query,state=True):
        """execute query on singleton db connection"""
        connection = cls.get_connection()
        try:
            cursor = connection.cursor()
        except pyodbc.ProgrammingError:
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor()
        cursor.execute(query)
        if state == True:
            result = cursor.fetchall()
            cursor.close()
            return result
        else:
            connection.commit()
            cursor.close()
#-----------------------------------------------------------------------
def print_Result(result:list):
    for row in result:
        print(f'Row # {result.index(row)} : {row}')
#-----------------------------------------------------------------------
#endregion General Functions

#region Query Functions

#region Select Query Functions
#-----------------------------------------------------------------------
def query_Select_All_From_Producto() -> str:
    return "SELECT * FROM [dbo].[Producto];"
#-----------------------------------------------------------------------
def query_Select_All_From_Caracteristica_By_Producto(producto:str,tipo:str) -> str:
    return f"""SELECT * FROM [dbo].[Caracteristica] JOIN [dbo].[Producto] \
        ON [Producto].nombre = '{producto}' \
        AND [dbo].[Producto].id = [dbo].[Caracteristica].id_producto\
        AND [Caracteristica].tipo = '{tipo}';"""
#-----------------------------------------------------------------------
#endregion Select Query Functions

#endregion Query Functions
#query = query_Select_All_From_Caracteristica_By_Producto("Retrato Mascota","TAMANO")
#print(query)
#results = DBConnection.execute_query(query,state=True)
#print(results)