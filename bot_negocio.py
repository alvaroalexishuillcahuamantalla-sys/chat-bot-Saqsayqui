from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bot_negocio', methods=['POST'])
def responder_numeros():
    mensaje_recibido = ""
    
    # 1. Extraemos estrictamente el texto del mensaje del JSON de AutoResponder
    if request.is_json:
        try:
            datos = request.get_json()
            mensaje_recibido = datos.get("message", "")
        except Exception:
            pass
    else:
        try:
            mensaje_recibido = request.data.decode('utf-8')
        except Exception:
            pass

    # Si no hay mensaje, respondemos vacío de inmediato
    if not mensaje_recibido:
        return jsonify({"replies": []})

    # 2. LIMPIEZA TOTAL: Nos quedamos SOLO con los números del mensaje del cliente
    # Esto elimina cualquier espacio, texto, puntos o basura alrededor.
    opcion = "".join(caracter for caracter in str(mensaje_recibido) if caracter.isdigit()).strip()

    # 3. EVALUACIÓN EXACTA
    # Ahora sí, comparamos el número limpio directamente para que no se confunda con nada más
    if opcion == "1":
        texto = (
            "📍 *Saqsayki - Tu mejor experiencia*\n"
            "🕒 *HORARIOS E INGRESO*\n\n"
            "📅 Lunes a domingo (incluyendo feriados)\n"
            "⏰ 9:30 a.m. a 5:30 p.m.\n\n"
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
    elif opcion == "2":
        texto = (
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
    elif opcion == "3":
        texto = (
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
    elif opcion == "4":
        texto = (
            "📍 *CÓMO LLEGAR A SAQSAYKI*\n\n"
            "🎒 Nos encontramos aproximadamente a 30 minutos a pie desde la Chicana Grande.\n\n"
            "🚕 En taxi podrás llegar en aproximadamente 15 minutos desde Chicana Grande.\n\n"
            "🗺️ *Google Maps:*\n"
            "http://maps.google.com/?q=Saqsayki"
            "\n📞 *Taxis recomendados:*\n"
            "• 926 050 769\n"
            "• 991 972 382\n\n"
            "🏍️ *Tours en cuatrimoto:*\n"
            "• 942 208 931\n\n"
            "💬 Escriba *menu* para volver al inicio"
        )
    elif opcion == "5":
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
                }
            ]
        })
    else:
        # Si llega cualquier otra cosa que no sea del 1 al 5, no respondemos nada
        return jsonify({"replies": []})

    return jsonify({"replies": [{"message": texto}]})

if __name__ == '__main__':
    app.run()
