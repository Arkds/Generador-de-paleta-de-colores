from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import random

app = Flask(__name__)

# Cargar el vectorizador y el modelo RandomForest
vectorizer = joblib.load('vectorizer_rf.pkl')
model = joblib.load('model_rf.pkl')

def predict_palette(text):
    text_vector = vectorizer.transform([text])
    return model.predict(text_vector)[0]

def combine_palettes(texts):
    combined_palette = set()
    for text in texts.split():
        palette = predict_palette(text)
        colors = palette.split(',')
        combined_palette.update(colors)
    # Seleccionar solo 3 colores al azar de la paleta combinada
    combined_palette = list(combined_palette)
    if len(combined_palette) > 3:
        combined_palette = random.sample(combined_palette, 3)
    return ','.join(combined_palette)

@app.route("/palette", methods=["POST"])
def get_palette():
    data = request.get_json()
    description = data.get("query", "")

    # Obtener la paleta combinada usando el texto proporcionado
    colors = combine_palettes(description)
    
    # Dividir los colores en una lista para el JSON de respuesta
    color_list = colors.split(',')

    return jsonify({"colors": color_list})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
