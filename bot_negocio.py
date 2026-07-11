from flask import Flask, request, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

# Configuración opcional por si deseas alertas en tu Telegram corporativo
TOKEN_TELEGRAM = "TU_TOKEN_DE_TELEGRAM"
CHAT_ID = "TU_CHAT_ID"

def enviar_a_telegram(texto):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": texto}, timeout=4)
    except:
        pass

@app.route('/bot_negocio', methods=['POST'])
def responder_cliente():
    datos = request.get_json()
    
    # Extraemos los datos enviados desde el flujo del celular
    mensaje_cliente = datos.get("message", "").strip().lower()
    telefono = datos.get("phone", "Cliente Anónimo")
    hora_actual = datetime.now().strftime("%H:%M:%S")
    
    # --- ÁRBOL DE DECISIONES INTERACTIVO CON FORMATO SOC ---
    if mensaje_cliente in ["hola", "buenas", "menu", "inicio"]:
        respuesta = {
            "reply": (
                "🏪 *[ASISTENTE VIRTUAL DE ATENCIÓN]*\n"
                "📊 *ESTADO:* OPERATIVO 24/7\n"
                "------------------------------------------\n"
                "¡Hola! Bienvenido a nuestro sistema de atención automatizado. "
                "Por favor, elige una opción respondiendo únicamente con el número:\n\n"
                "1️⃣ *Horarios de atención*\n"
                "2️⃣ *Catálogo de productos rápidos*\n"
                "3️⃣ *Ubicación de la tienda*\n"
                "4️⃣ *Hablar con el dueño / soporte*\n"
                "5️⃣ 📜 *Ver la Carta / Menú Completo (Imagen)*\n"
                "------------------------------------------\n"
                f"🕒 *Marca de tiempo:* {hora_actual}"
            )
        }
    elif mensaje_cliente == "1":
        respuesta = {
            "reply": (
                "🕒 *[REPORTE DE HORARIOS]*\n"
                "------------------------------------------\n"
                "• Lunes a Sábado: 9:00 AM a 8:00 PM\n"
                "• Domingos y Feriados: Cerrado\n"
                "------------------------------------------\n"
                f"📟 *Sesión:* {telefono} | {hora_actual}"
            )
        }
    elif mensaje_cliente == "2":
        respuesta = {
            "reply": (
                "📦 *[CATÁLOGO DE PRODUCTOS DISPONIBLES]*\n"
                "------------------------------------------\n"
                "• Producto 1 ➔ S/. 20.00\n"
                "• Producto 2 ➔ S/. 50.00\n"
                "• Producto 3 ➔ S/. 85.00\n"
                "------------------------------------------\n"
                "Si deseas realizar un pedido, marca la opción *4* para comunicarte con un asesor."
            )
        }
    elif mensaje_cliente == "3":
        respuesta = {
            "reply": (
                "📍 *[UBICACIÓN Y GEOLOCALIZACIÓN]*\n"
                "------------------------------------------\n"
                "• Dirección: Av. Universitaria 1234\n"
                "• Distrito: San Martín de Porres, Lima\n"
                "• Referencia: A 3 cuadras del Palacio de la Juventud.\n"
                "------------------------------------------\n"
                "¡Te esperamos en tienda!"
            )
        }
    elif mensaje_cliente == "4":
        respuesta = {
            "reply": (
                "👨‍💻 *[ALERTA: SOLICITUD DE ASESOR]*\n"
                "------------------------------------------\n"
                "• Asesor asignado: Conectándose...\n"
                "• Estado: En espera de atención humana.\n"
                "------------------------------------------\n"
                "Un asesor tomará tu chat en este mismo número en unos minutos. Déjanos tu consulta armada."
            )
        }
        # Notificación al dueño por Telegram usando el formato estructurado
        alerta_dueno = (
            f"⚠️ [ALERTA DE ATENCIÓN EN WHATSAPP]\n"
            f"👤 CLIENTE: {telefono}\n"
            f"⚡ ESTADO: Solicita hablar con humano.\n"
            f"🕒 HORA: {hora_actual}"
        )
        enviar_a_telegram(alerta_dueno)
    
    # 📜 OPCIÓN 5: ENVIAR LA CARTA EN FORMATO IMAGEN CON FORMATO DETALLADO
    elif mensaje_cliente == "5":
        respuesta = {
            "reply": (
                "📜 *[ENVÍO DE CARTA COMPLETA]*\n"
                "------------------------------------------\n"
                "Procesando archivo adjunto... Aquí tienes nuestra carta del día con todos los detalles y precios. ¡Disfrútala! 🍽️\n"
                "------------------------------------------"
            ),
            "file": "https://i.ibb.co/6w2zX9q/carta-ejemplo.jpg" 
            # 💡 REEMPLAZA esta URL por el enlace directo (.jpg o .png) de tu carta real
        }
        
    else:
        respuesta = {
            "reply": (
                "❌ *[COMANDO NO RECONOCIDO]*\n"
                "La opción ingresada no es válida.\n"
                "📝 Escribe la palabra *MENU* para volver a desplegar la lista de opciones."
            )
        }
        
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run()