import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from Models.nlp_helpers import clean_year_format

class CoffeeModel:
    def __init__(self, coffee_data):
        try:
            if isinstance(coffee_data, pd.DataFrame):
                print("Limpiando la columna 'Year'.")
                coffee_data['Year'] = coffee_data['Year'].astype(str)
                coffee_data['Year'] = coffee_data['Year'].apply(clean_year_format)
                
                print("Limpiando las columnas 'Country' y 'Metric'.")
                coffee_data['Country'] = coffee_data['Country'].str.lower().str.strip()
                coffee_data['Metric'] = coffee_data['Metric'].str.lower().str.strip()

                self.coffee_data = coffee_data
                print("DataFrame limpiado y almacenado.")

                self.models = {}
                metrics = coffee_data['Metric'].unique()

                for metric in metrics:
                    print(f"Entrenando el modelo para la métrica: {metric}")

                    metric_data = coffee_data[coffee_data['Metric'] == metric]

                    if metric_data.empty:
                        print(f"No hay suficientes datos para entrenar el modelo para la métrica '{metric}'.")
                        continue

                    metric_data = metric_data.dropna(subset=['ValueCoffee'])

                    if metric_data.empty:
                        print(f"No hay suficientes datos después de eliminar NaN en 'ValueCoffee' para la métrica '{metric}'.")
                        continue

                    metric_data = pd.get_dummies(metric_data, columns=['Country'], drop_first=True)

                    if 'Year' not in metric_data.columns:
                        print(f"Error en la columna 'Year' después de one-hot encoding para la métrica '{metric}'.")
                        continue

                    X = metric_data[['Year'] + [col for col in metric_data.columns if col.startswith('Country_')]]
                    y = metric_data['ValueCoffee']

                    if y.isnull().any():
                        print(f"'y' contiene NaN para la métrica '{metric}'.")
                        continue

                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                    if X_train.empty or y_train.empty:
                        print(f"No hay suficientes datos para entrenar el modelo para la métrica '{metric}'.")
                        continue

                    model = LinearRegression()
                    model.fit(X_train, y_train)

                    self.models[metric] = model
                    print(f"Modelo entrenado para la métrica '{metric}'.")

                if not self.models:
                    print("No se pudo entrenar ningún modelo debido a datos insuficientes.")
                    raise Exception("No models were trained.")

                print("Todos los modelos se han entrenado correctamente.")
            else:
                raise ValueError("Se esperaba un DataFrame de pandas.")

        except Exception as e:
            print(f"Error durante la inicialización o el entrenamiento del modelo: {e}")
            raise e
        

    def query_data(self, country, year, metric):
        """
        Predice el valor basado en el modelo entrenado para la métrica, país y año solicitados.
        Cambia la respuesta para datos históricos y futuros.
        """
        try:
            country = country.lower().strip()
            metric = metric.lower().strip()

            if metric not in self.models:
                return f"No se ha entrenado un modelo para la métrica '{metric}'."

            model = self.models[metric]
            X_columns = model.feature_names_in_

            country_column = f'Country_{country}'
            input_data = {col: 0 for col in X_columns}  
            input_data['Year'] = year 

            if country_column in X_columns:
                input_data[country_column] = 1
            else:
                return f"El país '{country}' no está disponible para predicción en la métrica '{metric}'."

            input_df = pd.DataFrame([input_data])

            predicted_value = model.predict(input_df)[0]
            formatted_value = format_number(predicted_value)  

            if year > 2019:
                if metric == 'production':
                    response = f"Se proyecta que {country.capitalize()} producirá aproximadamente {formatted_value} de toneladas de café en {year}."
                elif metric == 'export':
                    response = f"Se estima que {country.capitalize()} exportará cerca de {formatted_value} toneladas de café en {year}."
                elif metric == 'import':
                    response = f"Se espera que {country.capitalize()} importará alrededor de {formatted_value} toneladas de café en {year}."
                else:
                    response = f"Para {year}, se proyecta que el valor estimado para la métrica '{metric}' en {country.capitalize()} será de {formatted_value} toneladas de café."
                
                response += " **Nota:** Este valor es una predicción y puede no ser exacto."
            
            else:
                if metric == 'production':
                    response = f"En {year}, {country.capitalize()} produjo aproximadamente {formatted_value} de toneladas de café."
                elif metric == 'export':
                    response = f"En {year}, {country.capitalize()} exportó cerca de {formatted_value} toneladas de café."
                elif metric == 'import':
                    response = f"En {year}, {country.capitalize()} importó alrededor de {formatted_value} toneladas de café."
                else:
                    response = f"En {year}, el valor estimado para la métrica '{metric}' en {country.capitalize()} fue {formatted_value} toneladas de café."

            return response

        except Exception as e:
            return f"Error al procesar la consulta: {e}"

def format_number(value):

    if value >= 1e6:
        return f"{value / 1e6:.2f} millones"
    elif value >= 1e3:
        return f"{value / 1e3:.2f} mil"
    else:
        return f"{value:.2f}"
