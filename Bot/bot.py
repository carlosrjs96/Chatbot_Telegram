from pickletools import OpcodeInfo
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import Classes
import SQL

updater = Updater("5133692731:AAEnzvIWcMtIhvzPGMeSXYI6ej_Z_xcd0C0",
                  use_context=True)
#--------------------------------------------------------------------
# Flujos de productos
preguntas =  [
    "¿Cual tipo de lienzo te gustaria hacer?",     # Pregunta 0
    "¿Cual de los siguentes tamaños te interesa?", # Pregunta 1
    "¿Cuantas personas deseas en el retrato?",     # Pregunta 2
    "¿Cuantas mascotas deseas en el retrato?",     # Pregunta 3
    "Todos los retratos van con fondo de color liso. En caso de solicitar un fondo elaborado se cobra como adicional. ✨", # Pregunta 4
    "¿Desea hacer montaje de 2 fotos?" # Pregunta 5
]

def flujo(update: Update, context: CallbackContext):
    flujo_retrato:Classes.Flujo = context.user_data["Flujo"]
    if flujo_retrato.numero_pregunta == 0:
        #update.message.reply_photo(photo=open("./Images/Ilustrativo.jpg", 'rb'))
        #update.message.reply_photo(photo=open("./Images/Retrato.jpg"    , 'rb'))
        query = SQL.query_Select_All_From_Producto()
        results = SQL.DBConnection.execute_query(query,state=True)
        opciones = ""
        for opcion in results:
            opciones += f'{results.index(opcion)+1}. {opcion[1]}\n'
        update.message.reply_text(f"""{flujo_retrato.preguntas[0]}\n{opciones}""")

    elif flujo_retrato.numero_pregunta == 1:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.TAMANO.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opciones = ""
        for opcion in results:
            opciones += f'{results.index(opcion)+1}. {opcion[2]} ₡{opcion[4]}\n'
        update.message.reply_text(f"""{flujo_retrato.preguntas[1]}\n{opciones}""")

    elif flujo_retrato.numero_pregunta == 2:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.EXTRAPERSONA.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        tupla = results[0]
        opciones = f'₡{tupla[4]} por persona extra'
        update.message.reply_text(f"""{flujo_retrato.preguntas[2]} ({opciones})""")

    elif flujo_retrato.numero_pregunta == 3:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.EXTRAMASCOTA.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opciones = f'₡{results[0][4]} por mascota extra'
        update.message.reply_text(f"""{flujo_retrato.preguntas[3]} ({opciones})""")

    elif flujo_retrato.numero_pregunta == 4:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.FONDO.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opciones = ""
        for opcion in results:
            opciones += f'{results.index(opcion)+1}. {opcion[2]}\n'
        update.message.reply_text(f"""{flujo_retrato.preguntas[4]}\n{opciones}""")
    
    elif flujo_retrato.numero_pregunta == 5:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.MOTAJE.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opcionesPrecio = f'₡{results[0][4]} por montaje'
        opciones = "1. Si\n2. No"
        update.message.reply_text(f"""{flujo_retrato.preguntas[5]} ({opcionesPrecio}) \n{opciones}""")
    
    elif flujo_retrato.numero_pregunta == 6:
        update.message.reply_text(
        f"""Tu cotización es de un aproximado de ₡ {context.user_data["Flujo"].producto.get_Total()}.
- /Fecha_de_entrega mas proxima.
- /Cotizar_nuevo_producto.
- /Agente (Para hablar con un agente de ventas)
- /Salir.
""")

def recibe_info(update: Update, context: CallbackContext) -> int:
    flujo_retrato:Classes.Flujo = context.user_data["Flujo"]
    respuesta = update.message.text
    #update.message.reply_text(f"""{respuesta}""")
    if flujo_retrato.numero_pregunta == 0:
        query = SQL.query_Select_All_From_Producto()
        Opciones = SQL.DBConnection.execute_query(query,state=True) 
        opcion = Opciones[int(respuesta)-1]
        opcion = opcion[1]
        update.message.reply_text(f"""Elegiste {opcion}""")
        context.user_data["Flujo"].producto.nombre = opcion
    elif flujo_retrato.numero_pregunta == 1:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.TAMANO.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opcion = results[int(respuesta)-1]# <- AQUI ES DONDE SE VALIDA LA RESPUESTA
        update.message.reply_text(f"""Elegiste {opcion[2]}""")
        caracteristica = Classes.Caracteristica()
        caracteristica.nombre = opcion[2]
        caracteristica.tipo   = Classes.Tipo_Caracteristica.TAMANO
        caracteristica.precio = opcion[4]
        context.user_data["Flujo"].producto.caracteristicas.append(caracteristica)
    elif flujo_retrato.numero_pregunta == 2:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.EXTRAPERSONA.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opcion = results[0]# <- AQUI ES DONDE SE VALIDA LA RESPUESTA
        update.message.reply_text(f"""Elegiste {opcion[2]}""")
        for i in range(int(respuesta)):    
            caracteristica = Classes.Caracteristica()
            caracteristica.nombre = opcion[2]
            caracteristica.tipo   = Classes.Tipo_Caracteristica.EXTRAPERSONA
            caracteristica.precio = opcion[4]
            context.user_data["Flujo"].producto.caracteristicas.append(caracteristica)
    elif flujo_retrato.numero_pregunta == 3:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.EXTRAMASCOTA.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opcion = results[0]# <- AQUI ES DONDE SE VALIDA LA RESPUESTA
        update.message.reply_text(f"""Elegiste {opcion[2]}""")
        for i in range(int(respuesta)):    
            caracteristica = Classes.Caracteristica()
            caracteristica.nombre = opcion[2]
            caracteristica.tipo   = Classes.Tipo_Caracteristica.EXTRAMASCOTA
            caracteristica.precio = opcion[4]
            context.user_data["Flujo"].producto.caracteristicas.append(caracteristica)
    elif flujo_retrato.numero_pregunta == 4:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.FONDO.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opcion = results[int(respuesta)-1]# <- AQUI ES DONDE SE VALIDA LA RESPUESTA
        update.message.reply_text(f"""Elegiste {opcion[2]}""")
        caracteristica = Classes.Caracteristica()
        caracteristica.nombre = opcion[2]
        caracteristica.tipo   = Classes.Tipo_Caracteristica.FONDO
        caracteristica.precio = opcion[4]
        context.user_data["Flujo"].producto.caracteristicas.append(caracteristica)
    elif flujo_retrato.numero_pregunta == 5:
        if respuesta == "1":
            producto = context.user_data["Flujo"].producto.nombre 
            tipo = Classes.Tipo_Caracteristica.MOTAJE.name
            query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
            results = SQL.DBConnection.execute_query(query,state=True)
            opcion = results[0]# <- AQUI ES DONDE SE VALIDA LA RESPUESTA
            update.message.reply_text(f"""Elegiste {opcion[2]}""")
            caracteristica = Classes.Caracteristica()
            caracteristica.nombre = opcion[2]
            caracteristica.tipo   = Classes.Tipo_Caracteristica.MOTAJE
            caracteristica.precio = opcion[4]
            context.user_data["Flujo"].producto.caracteristicas.append(caracteristica)
    flujo_retrato.numero_pregunta += 1
    flujo(update,context)


#def receive_info(update: Update, context: CallbackContext) -> int:
#    # Extract the three capture groups
#    info = re.match(INFO_REGEX, update.message.text).groups()
#    # Using the first capture group as key, the second and third capture group are saved as a pair to the context.user_data
#    context.user_data[info[0]] = (info[1], info[2])
#
#    # Quote the information in the reply
#    update.message.reply_text(
#        f'So your {info[0]} {info[1]} {info[2]}, how interesting'
#    )
#--------------------------------------------------------------------

"""
message.from_user.id
message.from_user.first_name
message.from_user.last_name
message.from_user.username
"""
def saludo(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""¡Hola {update.effective_user.first_name}! Mi nombre es Myries Desing Bot,\
tu asistente virtual de Myries Desing. Si deseas obtener mas información puedes elegir algunas de las opciones de abajo.
- /Cotizar (Por medio del bot).
- /Agente (Para hablar con un agente de ventas).
            """)
def agente(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""Pronto uno de nuestros agentes te atendera en breve""")

def cotizar(update: Update, context: CallbackContext):
    context.user_data["Flujo"] = Classes.Flujo()
    context.user_data["Flujo"].preguntas = preguntas
    flujo(update,context)

def Fecha_de_entrega(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""Hola la fecha estimada de entrega esta para el 28/03/2022. 
¿Deseas realizar el pedido?
- /Si_realizar_el_pedido
- /No_realizar_el_pedido
""")

def salir(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""Gracias por todo, lo esperamos pronto""")
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

# --------------------------------------------------------------------------------------
# REGEX
saludo_Regex = r'^((H|h)ola|(B|b)uen|(H|h)ello|(H|h)i)'
respuesta_pregunta_numero = r'^(-?[0-9]+)'
# --------------------------------------------------------------------------------------
updater.dispatcher.add_handler(MessageHandler(Filters.regex(saludo_Regex), saludo))
#updater.dispatcher.add_handler(CommandHandler('Hola', saludo))recibe_info
updater.dispatcher.add_handler(MessageHandler(Filters.regex(respuesta_pregunta_numero), recibe_info))

updater.dispatcher.add_handler(CommandHandler('Cotizar', cotizar))
updater.dispatcher.add_handler(CommandHandler('Agente', agente))

updater.dispatcher.add_handler(CommandHandler('Fecha_de_entrega', Fecha_de_entrega))
updater.dispatcher.add_handler(CommandHandler('Cotizar_nuevo_producto', cotizar))
updater.dispatcher.add_handler(CommandHandler('Salir', salir))


updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
# Comienza el bot
updater.start_polling()
# Lo deja a la escucha. Evita que se detenga.
updater.idle()