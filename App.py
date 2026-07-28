# OrbitAssist AI Backend
# Handles user queries and generates responses

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Satellite Communication Knowledge Base
knowledge = {
    "frequency band": "Satellite communication uses frequency bands like L, S, C, X, Ku, and Ka bands for different applications.",
    "orbit": "Satellites operate in different orbits such as LEO, MEO, and GEO depending on their purpose.",
    "satellite communication": "Satellite communication uses satellites to transmit signals between ground stations and users.",
    "modulation": "Modulation techniques help encode information onto carrier signals for transmission."
}

@app.route("/")
def home():
    return "OrbitAssist AI Backend Running"

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("message", "").lower()

    response = "Sorry, I couldn't find information about this topic."

    for key in knowledge:
        if key in user_query:
            response = knowledge[key]
            break

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)