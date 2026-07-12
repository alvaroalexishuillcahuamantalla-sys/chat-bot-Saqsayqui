from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/bot_negocio', methods=['POST'])
def responder_cliente():
    mensaje_recibido = ""
    
    # 1. Sistema de lectura híbrido para capturar el mensaje sin importar el formato
    if request.is_json:
        datos = request.get_json()
        mensaje_recibido = datos.get("message", "")
    else:
        try:
            mensaje_recibido = request.data.decode('utf-8')
        except Exception:
            mensaje_recibido = ""
            
    if mensaje_recibido is None:
        mensaje_recibido = ""
        
    # Limpieza absoluta de espacios y conversión a minúsculas
    mensaje_cliente = str(mensaje_recibido).strip().lower()
    
    # 🚨 FILTRO PRIORITARIO: Buscamos si hay un número aislado del 1 al 5 en el mensaje
    # Usamos expresiones regulares para extraer quirúrgicamente el número
    numero_encontrado = re.search(r'\b([1-5])\b', mensaje_cliente)
    
    if numero_encontrado:
        opcion = numero_encontrado.group(1)
        
        if opcion == "1":
            texto_respuesta = (
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
            return generar_respuesta(texto_respuesta)
            
        elif opcion == "2":
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
            return generar_respuesta(texto_respuesta)
            
        elif opcion == "3":
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
            return generar_respuesta(texto_respuesta)
            
        elif opcion == "4":
            texto_respuesta = (
                "📍 *CÓMO LLEGAR A SAQSAYKI*\n\n"
                "🏃‍♂️‍➡️ Nos encontramos aproximadamente a 30 minutos a pie desde la Chicana Grande.\n\n"
                "🚕 En taxi podrás llegar en aproximadamente 15 minutos desde Chicana Grande.\n\n"
                "🗺️ *Google Maps:*\n"
                "https://maps.app.goo.gl/xrwjZyXT2iBeMiUr9\n\n"
                "📞 *Taxis recomendados:*\n"
                "• 926 050 769\n"
                "• 991 972 382\n\n"
                "🏍️ *Tours en cuatrimoto:*\n"
                "• 942 208 931\n\n"
                "💬 Escriba *menu* para volver al inicio"
            )
            return generar_respuesta(texto_respuesta)
            
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

    # 🚨 RESPUESTA POR DEFECTO: Si el mensaje no contiene los números 1, 2, 3, 4 o 5,
    # significa que es un saludo, un error, o la palabra "menu". Enviamos el menú completo.
    return mostrar_menu_principal()


def mostrar_menu_principal():
    texto = (
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
    return generar_respuesta(texto)

def generar_respuesta(texto_mensaje):
    return jsonify({"replies": [{"message": texto_mensaje}]})

if __name__ == '__main__':
    app.run()
