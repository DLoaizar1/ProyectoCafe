import re

COUNTRIES = ['Lao Peoples Democratic Republic','Finland','Rwanda','Liberia','Guatemala','Angola','Uganda','Italy','Brazil','Democratic Republic of Congo','Netherlands',
             'United States of America','Cameroon','Madagascar','Sri Lanka','Indonesia','Jamaica','Philippines','Germany','Cuba','Lithuania','Hungary','Cyprus','Malawi',
             'Switzerland','Estonia','Ecuador','Nigeria','El Salvador','Malta','Ethiopia','United Kingdom','Mexico','Sierra Leone','Sweden','Honduras','Viet Nam','Nicaragua',
             'Kenya','Unspecified EU stocks','Peru','Czechia','India','Côte d Ivoire','Croatia','Austria','Greece','Timor-Leste','Equatorial Guinea','Trinidad & Tobago',
             'Belgium/Luxembourg','Zimbabwe','Poland','Bulgaria','Central African Republic','Togo','Burundi','Guyana','Slovenia','Tunisia','Haiti','Ireland','Latvia',
             'Slovakia','Gabon','Guinea','Thailand','Norway','France','Dominican Republic','Luxembourg','Belgium','Japan','Yemen','Spain','Papua New Guinea','Venezuela',
             'Congo','Ghana','Denmark','Romania','Colombia','Panama','Bolivia','Tanzania','Nepal','Russian Federation','Zambia','Portugal','Costa Rica','Paraguay']


METRICS = ['Production', 'Re export', 'Domestic Consumption', 'Export', 'Import', 'Import Consumption', 'Green Coffee Inventories']

def extract_country(question):
    """
    Extrae el país mencionado en la pregunta del usuario.
    """
    for country in COUNTRIES:
        if country.lower() in question.lower():
            return country
    return "Unknown Country"

def extract_year(question):
    """
    Extrae el año mencionado en la pregunta del usuario.
    """
    match = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', question)
    if match:
        return int(match.group(0))
    return None

def extract_metric(question):
    """
    Extrae la métrica mencionada en la pregunta del usuario.
    """
    for metric in METRICS:
        if metric.lower() in question.lower():
            return metric
    return "Unknown Metric"

def clean_year_format(year_str):
    """
    Limpia el formato del año, tomando solo el primer año si es un rango como _1990_91.
    """
    if isinstance(year_str, str):  # Asegurarse de que el valor sea una cadena
        match = re.search(r'(\d{4})', year_str)
        if match:
            return int(match.group(1))  # Retorna el primer año encontrado
    return None
