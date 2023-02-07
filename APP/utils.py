'''UN MODULO EN PYTHON ES CUALQUIER ARCHIVO QUE TERMINE EN .PY, POR LO TANTO
LOS ARCHIVOS QUE TENEMOS EN EL EXPLORADOR PARA LOS EJERCICIOS TODOS SON MODULOS
DENTRO DE UN MODULO PODEMOS DEFINIR FUNCIONES, CLASES, VARIABLES...'''

#haremos una funcion para obtener la poblacion de un pais
#en este seg ejecicio de obtener la poblacion de un pais por año, creamos el dict con los
#añños tal cual aparece en el csv,lallave y le pasamos como pregunta el valor de la 
#poblacion
def get_population(country_dict):
    #keys = ['col','bol']
    #values = [300,400]
    population_dict = {
        '2022':country_dict(int['2022 population']),
        '2020':country_dict(int['2020 population']),
        '2015':country_dict(int['2015 population']),
        '2010':country_dict(int['2010 population']),
        '1990':country_dict(int['1990 population']),
        '1980':country_dict(int['1980 population']),
        '1970':country_dict(int['1970 population'])
        
    }
    #se debe enviar un array con labels es decir las llaves y otro con los valores
    #para eso miramos el ejemplo de el odulo charts.
    labels = population_dict.keys()#llaves o etiquetas
    values = population_dict.values()#valores
    return labels, values
#ya tenemos una solucion ahora vamos a unir las piezas, vamos a l archivo main.py y miramos
#que hemos trabajado con la busqueda de poblacion
#ahora vamos al archivo read_csv.py y reutilizar el codigo para leer.
#este modulo lee todo el csv y lo pasa a diccioario.



def population_by_country(data,country):
    result =list(filter(lambda item:item['country'] == country,data))
    return result
