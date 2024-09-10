from flask import Blueprint, render_template, request
from Models import coffe_models
import spacy
import re

# Carga del modelo NLP
nlp = spacy.load("en_core_web_sm")

# Mapeo de sinónimos de países
country_mapping = {
    "brazil": "Brazil",
    "brasil": "Brazil",
    "colombia": "Colombia",
    "vietnam": "Vietnam",
    "mexico": "Mexico",
    "usa": "United States",
    "united states": "United States",
}

chat_bp = Blueprint('chat', __name__)

def normalize_country_name(name):
    name = name.lower().strip()
    return country_mapping.get(name, name)

def extract_country(question):
    question = question.lower()
    doc = nlp(question)
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            return normalize_country_name(ent.text)
    return None

def extract_year(question):
    # Busca un año en el formato YYYY
    match = re.search(r'\b(19|20)\d{2}\b', question)
    if match:
        return int(match.group(0))
    return None

@chat_bp.route('/chat', methods=['POST'])
def chatbot():
    user_question = request.form['question']
    country = extract_country(user_question)
    year = extract_year(user_question)
    
    if country:
        if year:
            # Consultar la base de datos para obtener la información del país y año
            data = coffe_models.CoffeeDomesticConsumption.find_by_country_and_year(country, year)
            if data:
                value = getattr(data, f'_{year-1}_{year}', None)
                if value is not None:
                    response = f"Consumo total de café en {country} en el año {year}: {value} toneladas."
                else:
                    response = f"No se encontró información sobre el año {year} para el país {country}."
            else:
                response = f"No se encontró información sobre el país: {country} en el año {year}."
        else:
            # Consultar la base de datos para obtener la información total del país
            data = coffe_models.CoffeeDomesticConsumption.find_by_country(country)
            if data:
                response = f"Consumo total de café en {country}: {data[0].Total_domestic_consumption} toneladas."
            else:
                response = f"No se encontró información sobre el país: {country}."
    else:
        response = "No se pudo identificar el país en tu pregunta."
    
    return render_template('home.html', response=response)
