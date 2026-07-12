from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bot_bienvenida', methods=['POST'])
def responder_bienvenida():
    texto_menu = (
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
    return jsonify({"replies": [{"message": texto_menu}]})

if __name__ == '__main__':
    app.run(port=5002)
