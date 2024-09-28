import io
from flask import Blueprint, request, jsonify
from Models.coffe_models import CoffeeModel
import openai
from Models.nlp_helpers import extract_country, extract_year, extract_metric
import pandas as pd

chat_bp = Blueprint('chat', __name__)

try:
    df = pd.read_csv('D:/Users/loaiz/Desktop/Tesis/CoffeeDataUnified.csv')
    coffee_model = CoffeeModel(df)  
    print("Initial data loaded successfully.")
except Exception as e:
    print(f"Error al cargar el archivo CSV: {e}")
    coffee_model = None  # Para manejar errores si el archivo no se carga

openai.api_key = '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'

@chat_bp.route("/ask", methods=["POST"])
def ask_question():
    user_input = request.form["message"]
    try:
        # Asegurarnos de que el modelo esté inicializado correctamente antes de procesar la consulta
        if not coffee_model:
            return jsonify({"error": "Model not initialized correctly. Please check the data loading process."})
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a coffee data expert."},
                {"role": "user", "content": user_input}
            ]
        )

        # Parsear la respuesta
        parsed_question = response['choices'][0]['message']['content'].strip()

        # Extraer país, año y métrica de la pregunta usando las funciones auxiliares
        country = extract_country(parsed_question)
        year = extract_year(parsed_question)
        metric = extract_metric(parsed_question)

        # Asegurarnos de que se extrajeron los valores correctamente antes de consultar
        if not country or not year or not metric:
            return jsonify({"answer": "No se pudo interpretar la consulta. Por favor, proporciona un país, año y métrica válidos."})

        # Consultar el dataset con el modelo CoffeeModel
        result = coffee_model.query_data(country, year, metric)

        # Si no hay resultados, devolver un mensaje apropiado
        if not result or result == "No data available for your query.":
            return jsonify({"answer": "No data available for your query."})

        # Devolver la respuesta en formato JSON
        return jsonify({"answer": result})

    except Exception as e:
        # En caso de error, devolver un mensaje de error
        return jsonify({"error": str(e)})

def process_handle(handle):
    if hasattr(handle, 'read'):
        if isinstance(handle, io.IOBase):  
            return True
    else:
        print(f"handle is not a valid file object: {type(handle)}")
        return False

