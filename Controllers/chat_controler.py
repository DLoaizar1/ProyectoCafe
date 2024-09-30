import io
from flask import Blueprint, request, jsonify
from Models.coffe_models import CoffeeModel
import openai
from Models.nlp_helpers import extract_country, extract_year, extract_metric
import pandas as pd

chat_bp = Blueprint('chat', __name__)

try:
    df = pd.read_csv('D:/Users/loaiz/Desktop/Tesis/CoffeeDataUnified.csv')
    print("Archivo CSV cargado con éxito.")
    
    coffee_model = CoffeeModel(df)
    print("Modelos entrenados correctamente.")
    
except Exception as e:
    print(f"Error al cargar el archivo CSV o entrenar los modelos: {e}")
    coffee_model = None  

openai.api_key = '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'

@chat_bp.route("/ask", methods=["POST"])
def ask_question():
    user_input = request.form["message"]
    try:
        if not coffee_model:
            return jsonify({"error": "Model not initialized correctly. Please check the data loading process."})
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a coffee data expert."},
                {"role": "user", "content": user_input}
            ]
        )

        parsed_question = response['choices'][0]['message']['content'].strip()

        country = extract_country(parsed_question)
        year = extract_year(parsed_question)
        metric = extract_metric(parsed_question)

        if not country or not year or not metric:
            return jsonify({"answer": "No se pudo interpretar la consulta. Proporcione un país, año y métrica válidos."})

        result = coffee_model.query_data(country, year, metric)

        if not result or result == "No data available for your query.":
            return jsonify({"answer": "No data available for your query."})

        return jsonify({"answer": result})

    except Exception as e:
        # Manejo de excepciones
        return jsonify({"error": str(e)})
