import pandas as pd
from Models.nlp_helpers import clean_year_format

class CoffeeModel:
    def __init__(self, coffee_data):
        """
        Inicializa el modelo de café con los datos.
        """
        if isinstance(coffee_data, pd.DataFrame):
            # Convertir la columna 'Year' a tipo string antes de aplicar la limpieza
            coffee_data['Year'] = coffee_data['Year'].astype(str)
            coffee_data['Year'] = coffee_data['Year'].apply(clean_year_format)
            # Convertir los valores de la columna Country y Metric a minúsculas para coincidencias más flexibles
            coffee_data['Country'] = coffee_data['Country'].str.lower().str.strip()
            coffee_data['Metric'] = coffee_data['Metric'].str.lower().str.strip()
            self.coffee_data = coffee_data
        else:
            raise ValueError("Expected a pandas DataFrame")

    def query_data(self, country, year, metric):
        """
        Filtra los datos según país, año y métrica proporcionados.
        """
        # Convertir los valores de entrada a minúsculas para coincidencias flexibles
        country = country.lower().strip()
        metric = metric.lower().strip()

        # Depuración: Imprimir los valores de país, año y métrica que se están usando para la consulta
        print(f"Consultando datos para: País={country}, Año={year}, Métrica={metric}")
        
        # Filtrar los datos
        filtered_data = self.coffee_data[
            (self.coffee_data['Country'] == country) &
            (self.coffee_data['Year'] == year) &
            (self.coffee_data['Metric'] == metric)
        ]
        
        # Depuración: Imprimir el resultado de los datos filtrados
        print(f"Datos filtrados: {filtered_data}")
        
        if filtered_data.empty:
            return "No data available for your query."
        
        # Formatear los resultados en una respuesta legible
        results = filtered_data[['ValueCoffee']].to_dict(orient='records')
        
        # Crear una respuesta en texto para el chatbot
        result_text = f"Para {country.capitalize()} en el año {year}, los valores de {metric.capitalize()} son:\n"
        for i, result in enumerate(results, 1):
            result_text += f"{i}. {result['ValueCoffee']}\n"

        return result_text
