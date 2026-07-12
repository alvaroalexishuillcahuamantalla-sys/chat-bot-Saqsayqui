from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# ==========================
# RUTA PRINCIPAL
# ==========================

@app.route("/bot_negocio", methods=["POST"])
def responder_cliente():

    mensaje = extraer_mensaje(request)
    mensaje = limpiar_mensaje(mensaje)

    return clasificar_mensaje(mensaje)


# ==========================
# EXTRAER MENSAJE
# ==========================

def extraer_mensaje(request):
    try:
        if request.is_json:
            datos = request.get_json()
            return datos.get("message", "")
        return request.data.decode("utf-8")
    except:
        return ""


# ==========================
# LIMPIAR MENSAJE
# ==========================

def limpiar_mensaje(mensaje):

    mensaje = str(mensaje).lower().strip()

    mensaje = re.sub(r"[^\w\s]", "", mensaje)

    mensaje = re.sub(r"\s+", " ", mensaje)

    return mensaje


# ==========================
# CLASIFICADOR
# ==========================

def clasificar_mensaje(mensaje):

    # Saludos
    saludos = [
        "hola",
        "buenas",
        "buenos dias",
        "buenas tardes",
        "buenas noches",
        "hi",
        "hello"
    ]

    # Mostrar menú
    menu = [
        "menu",
        "menú",
        "inicio",
        "empezar",
        "volver"
    ]

    # Si es saludo
    if mensaje in saludos:
        return mostrar_menu()

    # Si escribe menu
    if mensaje in menu:
        return mostrar_menu()

    # Opciones numéricas
    if mensaje == "1":
        return generar_respuesta(response_horarios_ingreso())

    elif mensaje == "2":
        return generar_respuesta(response_precios_unitarios())

    elif mensaje == "3":
        return generar_respuesta(response_paquetes_promocionales())

    elif mensaje == "4":
        return generar_respuesta(response_como_llegar())

    elif mensaje == "5":
        return response_restaurante()

    # Cualquier otra cosa
    return mostrar_menu()


# ==========================
# RESPUESTAS
# ==========================

def response_horarios_ingreso():

    return (
        "📍 *Saqsayki - Tu mejor experiencia*\n\n"
        "🕒 *HORARIOS E INGRESO*\n\n"

        "📅 Lunes a domingo\n"
        "⏰ 9:30 a.m. - 5:30 p.m.\n\n"

        "🎟️ Adultos: S/7\n"
        "🎟️ Niños: S/4\n\n"

        "Incluye el acceso a todos los miradores y zonas turísticas.\n\n"

        "💬 Escriba *menu* para volver."
    )


def response_precios_unitarios():

    return (
        "💰 *PRECIOS UNITARIOS*\n\n"

        "🌊 Juegos Acuáticos\n"
        "• Caminata: S/5\n"
        "• Puente: S/5\n"
        "• Tirolesa: S/8\n"
        "• Puente Aéreo: S/8\n\n"

        "⛰️ Juegos de Altura\n"
        "• Columpio: S/20\n"
        "• Circuito: S/20\n\n"

        "💬 Escriba *menu* para volver."
    )


def response_paquetes_promocionales():

    return (
        "🎒 *PAQUETES*\n\n"

        "💦 Acuático S/25\n"
        "🧗 Aventurero S/35\n"
        "🔥 Full S/45\n\n"

        "💬 Escriba *menu* para volver."
    )


def response_como_llegar():

    return (
        "📍 *¿CÓMO LLEGAR?*\n\n"

        "🚕 Taxi: 15 minutos.\n"
        "🚶 Caminando: 30 minutos.\n\n"

        "🗺️ Google Maps:\n"
        "https://maps.app.goo.gl/xrwjZyXT2iBeMiUr9\n\n"

        "📞 Taxi:\n"
        "926050769\n"
        "991972382\n\n"

        "💬 Escriba *menu* para volver."
    )


def response_restaurante():

    return jsonify({

        "replies":[

            {

                "message":

                "🍽️ *Carta del Restaurante*\n\n"

                "Aquí puedes visualizar toda nuestra carta.\n\n"

                "Solo realizamos reservas para días festivos.\n\n"

                "💬 Escriba *menu* para volver.",

                "image":"https://i.ibb.co/6w2zX9q/carta-ejemplo.jpg"

            }

        ]

    })


# ==========================
# MENÚ
# ==========================

def mostrar_menu():

    texto = (
        "👋 ¡Bienvenido al *Parque Temático Saqsayki!* \n\n"

        "Seleccione una opción:\n\n"

        "1️⃣ Horarios e ingreso\n"
        "2️⃣ Precios unitarios\n"
        "3️⃣ Paquetes promocionales\n"
        "4️⃣ Cómo llegar\n"
        "5️⃣ Restaurante\n\n"

        "Escriba solamente el número de la opción."
    )

    return generar_respuesta(texto)


# ==========================
# RESPUESTA JSON
# ==========================

def generar_respuesta(texto):

    return jsonify({

        "replies":[

            {

                "message":texto

            }

        ]

    })


# ==========================

if __name__ == "__main__":
    app.run(debug=True)
