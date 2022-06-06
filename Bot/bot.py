from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram.ext.filters import Filters
import Classes
import SQL
import Util

_json = Util.load_Json('Config.json')
bot_token = _json['bot_token']
bot_chatID = _json['bot_chatID']
updater = Updater(bot_token,use_context=True)
#--------------------------------------------------------------------
# Flujos de productos
preguntas =  [
    "¿Cual tipo de lienzo te gustaria hacer?",     # Pregunta 0
    "¿Cual de los siguentes tamaños te interesa?", # Pregunta 1
    """- Todos los lienzos incluyen una persona
- En retratos de 20x20 son maximo 2 personas en total
¿Cuantas personas extra desea en el lienzo?""", # Pregunta 2
    """- Todos los lienzos incluyen una mascota
- En retratos de 20x20 son maximo 2 mascotas en total
¿Cuantas mascotas extra desea en el lienzo?""", # Pregunta 3
    "Todos los retratos van con fondo de color liso. En caso de solicitar un fondo elaborado se cobra como adicional. ✨", # Pregunta 4
    "¿Desea hacer montaje de 2 fotos?", # Pregunta 5
    "¿Cual es tu número telefónico?", # Pregunta 7
    "¿Cual es tu nombre de usuario en instagram?", # Pregunta 8
]

import requests

def telegram_bot_sendtext(bot_message):
   data = {
       'chat_id': bot_chatID,
       'text': bot_message
       }
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage'
   response = requests.get(send_text,params=data)
   return response.json()

def flujo(update: Update, context: CallbackContext):
    # PREGUNTAS
    # Pregunta 0 => "¿Cual tipo de lienzo te gustaria hacer?"
    if context.user_data["Flujo"].numero_pregunta == 0:
        update.message.reply_photo(photo=open("./Images/1.png", 'rb'))
        query = SQL.query_Select_All_From_Producto()
        results = SQL.DBConnection.execute_query(query,state=True)
        opciones = ""
        for opcion in results:
            opciones += f'{results.index(opcion)+1}. {opcion[1]}\n'
        update.message.reply_text(f"""{context.user_data["Flujo"].preguntas[0]}\n{opciones}""")
        print(update.message.chat.id)
    # Pregunta 1 => "¿Cual de los siguentes tamaños te interesa?"
    elif context.user_data["Flujo"].numero_pregunta == 1:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.TAMANO.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opciones = ""
        for opcion in results:
            opciones += f'{results.index(opcion)+1}. {opcion[2]} ₡{opcion[4]}\n'
        update.message.reply_text(f"""{context.user_data["Flujo"].preguntas[1]}\n{opciones}""")
    
    # Pregunta 2 => "¿Cuantas personas deseas en el retrato?"
    elif context.user_data["Flujo"].numero_pregunta == 2:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.EXTRAPERSONA.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        tupla = results[0]
        opciones = f'₡{tupla[4]} por persona extra'
        update.message.reply_text(f"""{context.user_data["Flujo"].preguntas[2]} ({opciones})""")
    
    # Pregunta 3 => "¿Cuantas mascotas deseas en el retrato?"
    elif context.user_data["Flujo"].numero_pregunta == 3:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.EXTRAMASCOTA.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opciones = f'₡{results[0][4]} por mascota extra'
        update.message.reply_text(f"""{context.user_data["Flujo"].preguntas[3]} ({opciones})""")
    
    # Pregunta 4 => "Todos los retratos van con fondo de color liso. En caso de solicitar un fondo elaborado se cobra como adicional. ✨"
    elif context.user_data["Flujo"].numero_pregunta == 4:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.FONDO.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opciones = ""
        for opcion in results:
            opciones += f'{results.index(opcion)+1}. {opcion[2]}\n'
        update.message.reply_text(f"""{context.user_data["Flujo"].preguntas[4]}\n{opciones}""")
    
    # Pregunta 5 => "¿Desea hacer montaje de 2 fotos?"
    elif context.user_data["Flujo"].numero_pregunta == 5:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.MOTAJE.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        results = SQL.DBConnection.execute_query(query,state=True)
        opcionesPrecio = f'₡{results[0][4]} por montaje'
        opciones = "1. Si\n2. No"
        update.message.reply_text(f"""{context.user_data["Flujo"].preguntas[5]} ({opcionesPrecio}) \n{opciones}""")
    
    # Pregunta
    elif context.user_data["Flujo"].numero_pregunta == 6:
        update.message.reply_text(
        f"""Tu cotización es de un aproximado de ₡ {context.user_data["Flujo"].producto.get_Total()}.
- /Realizar_pedido.
- /Cotizar_nuevo_producto.
- /Agente (Para hablar con un agente de ventas)
- /Salir.
""")
    # Pregunta 6 => "¿Cual es tu número telefónico?"
    elif context.user_data["Flujo"].numero_pregunta == 7:
        update.message.reply_text(f"""{context.user_data["Flujo"].preguntas[6]}""")    
    # Pregunta 7 => "¿Cual es tu nombre de usuario en instagram?" 
    elif context.user_data["Flujo"].numero_pregunta == 8:
        update.message.reply_text(f"""{context.user_data["Flujo"].preguntas[7]}""")
    elif context.user_data["Flujo"].numero_pregunta == 9:
        pedido = imprimirOrden(context.user_data["Flujo"])
        update.message.reply_text( pedido )
        test = telegram_bot_sendtext( pedido )
        update.message.reply_text(
        f"""
- /Cotizar_nuevo_producto.
- /Agente (Para hablar con un agente de ventas)
- /Salir.
""")    

def imprimirOrden(Flujo:Classes.Flujo):
    producto = ""
    for caracteristica in Flujo.producto.caracteristicas:
        producto += '\n----------------------------------------------------'
        producto += f'\n- {caracteristica.nombre:10}'
        producto += f'\n ₡{caracteristica.precio}'
    producto += '\n----------------------------------------------------'
    return f"""
### Resumen del pedido ###
============================================
Cliente : {Flujo.cliente.nombre}
Telefono : {Flujo.cliente.celular}
Telegram : {Flujo.cliente.user_Telegram}
Instagram : {Flujo.cliente.user_Instagram}
============================================
Producto: {Flujo.producto.nombre}
Detalles:{producto}
Total: {Flujo.producto.get_Total()}

Gracias por preferir Myrie's Design. Tu pedido fue tomando pronto nos contactaremos contigo para afinar detalles.
"""

def recibe_info_texto(update: Update, context: CallbackContext) -> int:
    if context.user_data["Flujo"].numero_pregunta == 8:
        context.user_data["Flujo"].cliente.user_Instagram = update.message.text
        context.user_data["Flujo"].numero_pregunta += 1
    else:
        unknown()
    flujo(update,context)

def recibe_info_numeros(update: Update, context: CallbackContext) -> int:
    opcion_elegida:int = int(update.message.text)
    #update.message.reply_text(f"""{opcion_elegida}""")
    # PREGUNTAS
    # Pregunta 0 => "¿Cual tipo de lienzo te gustaria hacer?"
    if context.user_data["Flujo"].numero_pregunta == 0:
        query = SQL.query_Select_All_From_Producto()
        Opciones = SQL.DBConnection.execute_query(query,state=True) 
        if validar_opciones_lista(Opciones,opcion_elegida):
            opcion = Opciones[int(opcion_elegida)-1]
            opcion = opcion[1]
            update.message.reply_text(f"Elegiste la opcion {opcion_elegida}. {opcion}")
            context.user_data["Flujo"].producto.nombre = opcion
            context.user_data["Flujo"].numero_pregunta += 1
        else:
            update.message.reply_text(f"Ingrese una opcion valida")

    # Pregunta 1 => "¿Cual de los siguentes tamaños te interesa?" 
    elif context.user_data["Flujo"].numero_pregunta == 1:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.TAMANO.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        Opciones = SQL.DBConnection.execute_query(query,state=True)
        if validar_opciones_lista(Opciones,opcion_elegida):
            opcion = Opciones[int(opcion_elegida)-1]# <- AQUI ES DONDE SE VALIDA LA RESPUESTA
            update.message.reply_text(f"""Elegiste {opcion[2]}""")
            caracteristica = Classes.Caracteristica()
            caracteristica.nombre = opcion[2]
            caracteristica.tipo   = Classes.Tipo_Caracteristica.TAMANO
            caracteristica.precio = opcion[4]
            context.user_data["Flujo"].producto.caracteristicas.append(caracteristica)
            context.user_data["Flujo"].numero_pregunta += 1
        else:
            update.message.reply_text(f"Ingrese una opcion valida")
    
    # Pregunta 2 => "¿Cuantas personas deseas en el retrato?"
    elif context.user_data["Flujo"].numero_pregunta == 2:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.EXTRAPERSONA.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        Opciones = SQL.DBConnection.execute_query(query,state=True)
        cantidad_personas = opcion_elegida
        caracteristicas   = context.user_data["Flujo"].producto.caracteristicas
        if validar_opciones_cantidad(cantidad_personas,caracteristicas):
            opcion = Opciones[0]# <- AQUI ES DONDE SE VALIDA LA RESPUESTA
            update.message.reply_text(f"""Elegiste {opcion[2]}""")
            for i in range(cantidad_personas):    
                caracteristica = Classes.Caracteristica()
                caracteristica.nombre = opcion[2]
                caracteristica.tipo   = Classes.Tipo_Caracteristica.EXTRAPERSONA
                caracteristica.precio = opcion[4]
                context.user_data["Flujo"].producto.caracteristicas.append(caracteristica)
            context.user_data["Flujo"].numero_pregunta += 1
        else:
            update.message.reply_text(f"Ingrese una cantidad valida de personas")
    
    # Pregunta 3 => "¿Cuantas mascotas deseas en el retrato?"
    elif context.user_data["Flujo"].numero_pregunta == 3:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.EXTRAMASCOTA.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        Opciones = SQL.DBConnection.execute_query(query,state=True)
        cantidad_mascotas = opcion_elegida
        caracteristicas   = context.user_data["Flujo"].producto.caracteristicas
        if validar_opciones_cantidad(cantidad_mascotas,caracteristicas):
            opcion = Opciones[0]# <- AQUI ES DONDE SE VALIDA LA RESPUESTA
            update.message.reply_text(f"""Elegiste {opcion[2]}""")
            for i in range(cantidad_mascotas):    
                caracteristica = Classes.Caracteristica()
                caracteristica.nombre = opcion[2]
                caracteristica.tipo   = Classes.Tipo_Caracteristica.EXTRAMASCOTA
                caracteristica.precio = opcion[4]
                context.user_data["Flujo"].producto.caracteristicas.append(caracteristica)
            context.user_data["Flujo"].numero_pregunta += 1
        else:
            update.message.reply_text(f"Ingrese una cantidad valida de mascotas")

    # Pregunta 4 => "Todos los retratos van con fondo de color liso. En caso de solicitar un fondo elaborado se cobra como adicional. ✨"
    elif context.user_data["Flujo"].numero_pregunta == 4:
        producto = context.user_data["Flujo"].producto.nombre 
        tipo = Classes.Tipo_Caracteristica.FONDO.name
        query = SQL.query_Select_All_From_Caracteristica_By_Producto(producto,tipo)
        Opciones = SQL.DBConnection.execute_query(query,state=True)
        if validar_opciones_lista(Opciones,opcion_elegida):
            opcion = Opciones[int(opcion_elegida)-1]# <- AQUI ES DONDE SE VALIDA LA RESPUESTA
            update.message.reply_text(f"""Elegiste {opcion[2]}""")
            caracteristica = Classes.Caracteristica()
            caracteristica.nombre = opcion[2]
            caracteristica.tipo   = Classes.Tipo_Caracteristica.FONDO
            caracteristica.precio = opcion[4]
            context.user_data["Flujo"].producto.caracteristicas.append(caracteristica)
            context.user_data["Flujo"].numero_pregunta += 1
        else:
            update.message.reply_text(f"Ingrese una opcion valida")
    # Pregunta 5 => "¿Desea hacer montaje de 2 fotos?"
    elif context.user_data["Flujo"].numero_pregunta == 5:
        if opcion_elegida == 1:
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
            context.user_data["Flujo"].numero_pregunta += 1
        elif opcion_elegida > 2 or opcion_elegida <=0:
            update.message.reply_text(f"Ingrese una opcion valida")
        else:
            context.user_data["Flujo"].numero_pregunta += 1
    elif context.user_data["Flujo"].numero_pregunta == 7:
        if len(update.message.text) == 8:
            celular = opcion_elegida
            context.user_data["Flujo"].cliente.celular = celular 
            context.user_data["Flujo"].numero_pregunta += 1
        else:
            update.message.reply_text(f"Ingrese una número telefónico valido")
    else:
        unknown()
    flujo(update,context)

# Validaciones
# --------------------------------------------------------------------------------------------------
def validar_opciones_lista(opciones:list,opcion_elegida:int):
    if opcion_elegida > 0 and opcion_elegida <= len(opciones):
        return True
    return False
# --------------------------------------------------------------------------------------------------
def validar_opciones_cantidad(cantidad:int,caracteristicas:list[Classes.Caracteristica]):
    if cantidad < 0:
        return False
    for caracteristica in caracteristicas:
        if caracteristica.tipo == Classes.Tipo_Caracteristica.TAMANO and \
            "20X20" in caracteristica.nombre.upper() and cantidad >1:
            return False
    return True
# --------------------------------------------------------------------------------------------------

"""
message.from_user.id
message.from_user.first_name
message.from_user.last_name
message.from_user.username
"""
def realizar_pedido(update: Update, context: CallbackContext):
    context.user_data["Flujo"].numero_pregunta += 1
    context.user_data["Flujo"].cliente.nombre = f'{update.effective_user.first_name} {update.effective_user.last_name}'
    context.user_data["Flujo"].cliente.user_Telegram = update.effective_user.username
    #context.user_data["Flujo"].cliente.celular = phone
    flujo(update,context)

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

def telefono(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)
    print(update.message.text)

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
        "Sorry '%s' no es un commando invalido" % update.message.text)  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

# --------------------------------------------------------------------------------------
# REGEX
saludo_Regex = r'^((H|h)ola|(B|b)uen|(H|h)ello|(H|h)i)'
respuesta_pregunta_numero = r'^(-?[0-9]+)'
# --------------------------------------------------------------------------------------
updater.dispatcher.add_handler(MessageHandler(Filters.regex(saludo_Regex), saludo))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(respuesta_pregunta_numero), recibe_info_numeros))

updater.dispatcher.add_handler(CommandHandler('Cotizar', cotizar))
updater.dispatcher.add_handler(CommandHandler('Realizar_pedido', realizar_pedido))
updater.dispatcher.add_handler(CommandHandler('Agente', agente))


updater.dispatcher.add_handler(CommandHandler('Fecha_de_entrega', Fecha_de_entrega))
updater.dispatcher.add_handler(CommandHandler('Cotizar_nuevo_producto', cotizar))
updater.dispatcher.add_handler(CommandHandler('Salir', salir))


updater.dispatcher.add_handler(MessageHandler(Filters.text, recibe_info_texto))
#updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
# Comienza el bot
updater.start_polling()
# Lo deja a la escucha. Evita que se detenga.
updater.idle()