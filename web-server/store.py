"""primero se creo el direcorio web-server con mmkdir en la terminal ubuntu, luego se
se creo el ambiente virtual para este,se activo, y se descargo la libreria requests
que es la misma que estamos importando aca, luego creamos el archivo llamado store.py
en este creamos la funcion para comunicarnos o consumir la api fake de platzi, asi podemos
obtener informacion de la api"""

import requests
#creamos la funcion y accedemos con la direccion https
def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    #accedemos al status code, para verificar si la comunicacion esta bien
    print(r.status_code)
    #algo importante es saber la respuesta, que nos devuelve la api
    print(r.text)
    #luego creamos el archivo principal main.py e importamos el modulo store
    #preguntamos que tipo de dato es.
    print(type(r.text))
    #es un string grande por eso primero hhay que transformarlo con python, por eso
    #asi como string no se puede iterar
    categories = r.json()
    #pedimos que lo transforme a formato json, asi pytho si lo reconoce para iterar
    #ahora lo recorremos con unn for por categorias
    for category in categories:
        #debemos saber si la categoria que queremos se llama name...
        print(category['name'])
    