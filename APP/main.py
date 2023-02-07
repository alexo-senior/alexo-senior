
"""para llamar un modulo en python siempre se usa la palabra import y el nombre del
archivo, en este caso vamos a impórtar modulo, que fue eel nombre dado al archivo
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
    data = read_csv.read_csv(
        'data.csv')
    data = list(
        filter(lambda item: item['continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population percentage'], data))
    charts.generate_pie_chart(countries, percentages)

    country = input('Type Country => ')
    #colocamos un imput para solicitar la preferencia de informacion
    
#usamo una varible le pasamos el modulo utils que contiene el dict y nos va a buscar los 
#valores de poblacion poor pais, le pasamos la data que es la lectura y el pais que esta en
#el input.
    result = utils.Population_by_Country(data, country,)
    # el resultado debe mayor a cero, una vez encontro a ese pais se lo pasa a la variable
    # country en la posicion cero y luego a la funcion get_population
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        # print(keys,values)
        charts.generate_bar_chart(labels, values)
    
    
    if __name__ == '__main__':
        run()
        
    

#se le pasa a la funcion la data (dict), y el nombre del pais que se quiere la info
#print(result)
#[{'country': 'colombia', 'population': 1000




    
