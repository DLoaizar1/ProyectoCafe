import re
import unicodedata

COUNTRIES = ['Lao Peoples Democratic Republic', 'Finland', 'Rwanda', 'Liberia', 'Guatemala', 'Angola', 'Uganda', 'Italy', 'Brazil', 'Democratic Republic of Congo', 'Netherlands',
             'United States of America', 'Cameroon', 'Madagascar', 'Sri Lanka', 'Indonesia', 'Jamaica', 'Philippines', 'Germany', 'Cuba', 'Lithuania', 'Hungary', 'Cyprus', 'Malawi',
             'Switzerland', 'Estonia', 'Ecuador', 'Nigeria', 'El Salvador', 'Malta', 'Ethiopia', 'United Kingdom', 'Mexico', 'Sierra Leone', 'Sweden', 'Honduras', 'Viet Nam', 'Nicaragua',
             'Kenya', 'Unspecified EU stocks', 'Peru', 'Czechia', 'India', 'Côte d Ivoire', 'Croatia', 'Austria', 'Greece', 'Timor-Leste', 'Equatorial Guinea', 'Trinidad & Tobago',
             'Belgium/Luxembourg', 'Zimbabwe', 'Poland', 'Bulgaria', 'Central African Republic', 'Togo', 'Burundi', 'Guyana', 'Slovenia', 'Tunisia', 'Haiti', 'Ireland', 'Latvia',
             'Slovakia', 'Gabon', 'Guinea', 'Thailand', 'Norway', 'France', 'Dominican Republic', 'Luxembourg', 'Belgium', 'Japan', 'Yemen', 'Spain', 'Papua New Guinea', 'Venezuela',
             'Congo', 'Ghana', 'Denmark', 'Romania', 'Colombia', 'Panama', 'Bolivia', 'Tanzania', 'Nepal', 'Russian Federation', 'Zambia', 'Portugal', 'Costa Rica', 'Paraguay']

def load_translations(file_path):
    translations = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    translations[parts[0].strip().lower()] = parts[1].strip().lower()
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
    return translations

COUNTRY_TRANSLATIONS_PATH = r'D:\Users\loaiz\Desktop\Tesis\country_translations.txt'
METRIC_TRANSLATIONS_PATH = r'D:\Users\loaiz\Desktop\Tesis\metric_translation.txt'

country_translations = load_translations(COUNTRY_TRANSLATIONS_PATH)
metric_translations = load_translations(METRIC_TRANSLATIONS_PATH)

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

def extract_country(question):
    question_normalized = remove_accents(question.lower())
    for country_es, country_en in country_translations.items():
        country_es_normalized = remove_accents(country_es)
        if country_es_normalized in question_normalized:
            return country_en.lower()
    return 'unknown country'

def extract_year(question):
    match = re.search(r'\b(19[0-9]{2}|2[0-9]{3})\b', question)
    if match:
        return int(match.group(0))
    return None

def extract_metric(question):
    question_lower = question.lower()
    for metric_es_pattern, metric_en in metric_translations.items():
        if re.search(metric_es_pattern, question_lower):
            return metric_en.lower()
    return "unknown metric"

def clean_year_format(year_str):
    if isinstance(year_str, str): 
        match = re.search(r'(\d{4})', year_str)
        if match:
            return int(match.group(1))
    return None