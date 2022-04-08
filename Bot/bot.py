from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
  
updater = Updater("5133692731:AAEnzvIWcMtIhvzPGMeSXYI6ej_Z_xcd0C0",
                  use_context=True)


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
    update.message.reply_photo(photo=open("./Images/Ilustrativo.jpg", 'rb'))
    update.message.reply_photo(photo=open("./Images/Retrato.jpg"    , 'rb'))
    update.message.reply_text(
        f"""¿Cual de tipo de lienzo te gustaria hacer?
- /Tipo_Retrato.
- /Tipo_Ilustracion.
            """)

def Tipo_Retrato(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""¿Cual de los siguentes tamaños te interesa?
Retrato de 1 mascota:
/1_Retrato_de_20x20_cm ₡18 000
/2_Retrato_de_30x40_cm ₡28 000
/3_Retrato_de_40x50_cm ₡38 000

Retrato de rostro 1 persona:
/4_Retrato_de_20x20_cm ₡23 000
/5_Retrato_de_30x40_cm ₡33 000
/6_Retrato_de_40x50_cm ₡43 000
""")

def Agregar_Extra(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""¿Deseas agregar un extra?
/Persona_extra ₡5000 c/u
/Mascota_extra ₡3000 c/u
/No_Agregar_Extra
""")


def Agregar_Persona_Extra(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""¿Cuantas personas extra deseas agregar?""")

def Agregar_Mascota_Extra(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""¿Cuantas mascotas extra deseas agregar?""")

def Fondo(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""Todos los retratos van con fondo de color liso. En caso de solicitar un fondo elaborado se cobra como adicional. ✨
- /Color_Liso.
- /Elaborado ( Sujeto a cotización por parte de la creadora ).
""")

def Cotizacion(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""Tu cotización es de un aproximado de ₡ 27 000. 
- /Fecha_de_entrega mas proxima.
- /Cotizar_nuevo_producto
- /Agente (Para hablar con un agente de ventas)
- /Salir
""")

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


def menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.""")

  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /geeks - To get the GeeksforGeeks URL""")
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
updater.dispatcher.add_handler(CommandHandler('Hola', saludo))

updater.dispatcher.add_handler(CommandHandler('Cotizar', cotizar))
updater.dispatcher.add_handler(CommandHandler('Agente', agente))

updater.dispatcher.add_handler(CommandHandler('Tipo_Retrato', Tipo_Retrato))
#updater.dispatcher.add_handler(CommandHandler('Tipo_Ilustracion', Tipo_Ilustracion))

updater.dispatcher.add_handler(CommandHandler('1_Retrato_de_20x20_cm', Agregar_Extra))
updater.dispatcher.add_handler(CommandHandler('2_Retrato_de_30x40_cm', Agregar_Extra))
updater.dispatcher.add_handler(CommandHandler('3_Retrato_de_40x50_cm', Agregar_Extra))
updater.dispatcher.add_handler(CommandHandler('4_Retrato_de_20x20_cm', Agregar_Extra))
updater.dispatcher.add_handler(CommandHandler('5_Retrato_de_30x40_cm', Agregar_Extra))
updater.dispatcher.add_handler(CommandHandler('6_Retrato_de_40x50_cm', Agregar_Extra))

updater.dispatcher.add_handler(CommandHandler('Persona_extra', Agregar_Persona_Extra))
updater.dispatcher.add_handler(CommandHandler('Mascota_extra', Agregar_Mascota_Extra))
updater.dispatcher.add_handler(CommandHandler('No_Agregar_Extra', Fondo))

updater.dispatcher.add_handler(CommandHandler('Color_Liso', Cotizacion))
updater.dispatcher.add_handler(CommandHandler('Elaborado', Cotizacion))

updater.dispatcher.add_handler(CommandHandler('Fecha_de_entrega', Fecha_de_entrega))
updater.dispatcher.add_handler(CommandHandler('Cotizar_nuevo_producto', cotizar))
updater.dispatcher.add_handler(CommandHandler('Salir', salir))


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
# Comienza el bot
updater.start_polling()
# Lo deja a la escucha. Evita que se detenga.
updater.idle()