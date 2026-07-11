from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/bot_negocio', methods=['POST'])
def responder_cliente():
    datos = request.get_json()
    
    # Extraemos el mensaje del cliente de forma segura y lo limpiamos
    mensaje_recibido = datos.get("message", "")
    if mensaje_recibido is None:
        mensaje_recibido = ""
        
    mensaje_cliente = str(mensaje_recibido).strip().lower()
    telefono = datos.get("phone", "Cliente Anónimo")
    
    # --- ÁRBOL DE DECISIONES CON LA INFORMACIÓN REAL DE SAQSAYKI ---
    
    # Menú Principal
    if mensaje_cliente in ["hola", "buenas", "menu", "inicio", "p", "buenos dias", "buenas tardes", "*", ""]:
        texto_respuesta = (
            "¡Buenas noches! ✨\n\n"
            "Bienvenido(a) al *Parque Temático Saqsayki*\n\n"
            "Vive una experiencia única llena de aventura, diversión y naturaleza.\n\n"
            "📌 *Seleccione una opción escribiendo el número:*\n\n"
            "1️⃣ Horarios e ingreso\n"
            "2️⃣ Precios unitarios de juegos\n"
            "3️⃣ Paquetes promocionales\n"
            "4️⃣ Cómo llegar\n"
            "5️⃣ Restaurante 🍽️ (Ver carta completa)\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "💡 Ingrese una de las opciones\n\n"
            "📌 *Comandos:* Escriba *menu* para ver este mensaje nuevamente\n\n"
            "📍 Saqsayki - Tu mejor experiencia"
        )
        return jsonify({"replies": [{"message": texto_respuesta}]})

    # Opción 1: Horarios e Ingreso
    elif mensaje_cliente == "1":
        texto_respuesta = (
            "🕒 *HORARIOS E INGRESO*\n\n"
            "📅 Lunes a domingo (incluyendo feriados)\n"
            "⏰ 9:30 a.m. a 5:50 p.m.\n\n"
            "🎟️ *Precios de ingreso:*\n"
            "• Adultos: S/ 7.00\n"
            "• Niños: S/ 4.00\n\n"
            "✅ *El ingreso incluye:*\n"
            "• Mano Gigante del Inca\n"
            "• Bosque Encantado de los Duendes\n"
            "• Mano de Choclo de Oro\n"
            "• Trilogía Andina\n"
            "• Diversos miradores turísticos\n\n"
            "💬 Escriba *menu* para volver al inicio"
        )
        return jsonify({"replies": [{"message": texto_respuesta}]})

    # Opción 2: Precios Unitarios de Juegos
    elif mensaje_cliente == "2":
        texto_respuesta = (
            "💰 *PRECIOS UNITARIOS DE JUEGOS*\n\n"
            "🌊 *Juegos Acuáticos*\n"
            "• Caminata en línea — S/ 5.00\n"
            "• Puente acuático — S/ 5.00\n"
            "• Tirolesa acuática — S/ 8.00\n"
            "• Puente aéreo — S/ 8.00\n\n"
            "⛰️ *Juegos de Altura*\n"
            "• Columpio Extremo 'Vuelo del Cóndor' — S/ 20.00\n"
            "• Circuito de 21 obstáculos extremos — S/ 20.00\n\n"
            "💬 Escriba *menu* para volver al inicio"
        )
        return jsonify({"replies": [{"message": texto_respuesta}]})

    # Opción 3: Paquetes Promocionales
    elif mensaje_cliente == "3":
        texto_respuesta = (
            "🎒 *PAQUETES PROMOCIONALES*\n\n"
            "💦 *Paquete Acuático — S/ 25.00*\n"
            "• Entrada al parque\n"
            "• Puente acuático\n"
            "• Caminata en línea\n"
            "• Tirolesa acuática\n"
            "• Puente aéreo\n\n"
            "🧗 *Paquete Aventurero — S/ 35.00*\n"
            "• Entrada al parque\n"
            "• Columpio extremo\n"
            "• Circuito de 21 obstáculos\n"
            "• Puente acuático\n\n"
            "🔥 *Paquete Full — S/ 45.00*\n"
            "• Entrada al parque\n"
            "• Columpio extremo\n"
            "• Circuito de 21 obstáculos\n"
            "• Tirolesa acuática\n"
            "• Caminata en línea\n"
            "• Puente aéreo\n"
            "• Puente acuático\n\n"
            "💬 Escriba *menu* para volver al inicio"
        )
        return jsonify({"replies": [{"message": texto_respuesta}]})

    # Opción 4: Cómo Llegar
    elif mensaje_cliente == "4":
        texto_respuesta = (
            "📍 *CÓMO LLEGAR A SAQSAYKI*\n\n"
            "🏃‍♂️‍➡️ Nos encontramos aproximadamente a 30 minutos a pie desde la Chicana Grande.\n\n"
            "🚕 En taxi podrás llegar en aproximadamente 15 minutos desde Chicana Grande.\n\n"
            "🗺️ *Google Maps:*\n"
            "http://maps.google.com/?q=-13.5042,-71.9791\n\n" # Puedes cambiar esta URL por tu link directo si gustas
            "📞 *Taxis recomendados:*\n"
            "• 926 050 769\n"
            "• 991 972 382\n\n"
            "🏍️ *Tours en cuatrimoto:*\n"
            "• 942 208 931\n\n"
            "💬 Escriba *menu* para volver al inicio"
        )
        return jsonify({"replies": [{"message": texto_respuesta}]})
    
    # Opción 5: Restaurante + Envío Automático de la Imagen de la Carta
    elif mensaje_cliente == "5":
        return jsonify({
            "replies": [
                {
                    "message": (
                        "🍽️ *CARTA DEL RESTAURANTE SAQSAYKI*\n\n"
                        "Aquí está nuestra carta completa con todos nuestros platillos.\n\n"
                        "📌 *Nota:* Solo realizamos reservas para días festivos y eventos especiales.\n\n"
                        "¿Tienes alguna consulta? Escríbenos sin problema, estamos para ayudarte.\n\n"
                        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        "💬 Escriba *menu* para volver al inicio"
                    ),
                    "image": "https://i.ibb.co/6w2zX9q/carta-ejemplo.jpg" 
                    # 💡 Reemplaza esta URL de arriba por el enlace directo de la foto de tu carta real (.jpg)
                }
            ]
        })
        
    # En caso de que marquen algo incorrecto
    else:
        texto_respuesta = (
            "❌ *[COMANDO NO RECONOCIDO]*\n\n"
            "La opción ingresada no es válida.\n\n"
            "📝 Escribe la palabra *menu* para volver a desplegar la lista de opciones del parque."
        )
        return jsonify({"replies": [{"message": texto_respuesta}]})

if __name__ == '__main__':
    app.run()
