
"""para llamar un modulo en python siempre se usa la palabra import y el nombre del
archivo, en este caso vamos a impórtar modulo, que fue el nombre dado al archivo
y añadir de una vez la funcion que creamos llamada get_population
una buena practica es llamar al modulo de una forma diciente acorde a lo que hace
siendo una herramienta de trabajo, ademas es de notar que cualquier archivo que creamos 
en el modulo base se puede llamar desde otra ubicacion y ejecutar con el nombre de la
variable separado por un punto y el nombre del modulo"""

import utils # este modulo fue creado por mi con una funcion, y de esa manera lo 
#estoy llamando , con un import para aplicarlo a mi ejercicio.
#como me va a retornar dos valores los puedo asignar como variables
import read_csv #para leer el csv
import charts #para graficar el codigo
import pandas as pd


'''keys,values = utils.get_population()'''
'''print(keys,values)
"""como vimos en el archivo modulo creamos la varibale 'a', y le asignamos un nombre
luego a llamamos desde main.py para imprimirla, y nos da el nombre que le asignamos"""
print(utils.a)

data = [
    {
        "country": "colombia",
        "population":1000
        
    },
    {
        "country":"bolivia",
        "population":500
        
    }
]'''
#definimos la funcion, unna variable data, le pasamos la funcion y le modulo con 
#la ubicacion del archivo csv


def run():
    #esta parte se comenta ya que se va a usar la libreria panda
    '''
    data = list(
        filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population percentage'], data))
    '''
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Africa']
    countries = df['Country'].values
    percentages = df['World Population percentage'].values
    charts.generate_pie_chart(countries, percentages)

    data = read_csv.read_csv(
        'RUTA PLATZI\PROJECT\py-project\APP\data.csv')
    country = input('Type Country => ')
    print(country)

    result = utils.Population_by_Country(data, Country,)

    
#usamos una varible le pasamos el modulo utils que contiene el dict y nos va a buscar los 
#valores de poblacion por pais, le pasamos la data que es la lectura y el pais que esta en
#el input.
    if len(result) > 0:
        Country = result[0]
        print(country)
        labels, values = utils.get_population(Country)
        # print(keys,values)
        charts.generate_bar_chart(country['Country'], labels, values)
    # el resultado debe ser mayor a cero, una vez encontro a ese pais se lo pasa a la variable
    # country en la posicion cero y luego a la funcion get_population
    
    
    
    
    if __name__ == '__main__':
        run()
        
    

#se le pasa a la funcion la data (dict), y el nombre del pais que se quiere la info
#print(result)
#[{'country': 'colombia', 'population': 1000



run()
    
