
import store #importamos store todas sus funciones

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI() # instanciamos la importacion de fastapi
#decorador con la ruta para acceder

@app.get('/')
def get_list(): #creamos la funcion para obtener la info
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list(): 
    #return {'name':'Platzi'}
    return """<h1> hola soy una pagina en HTML</H1>
            <p> soy un ejemplo de parrafo</p>   
"""



 
#creamos la funcion run
def run():
    store.get_categories()
# se debe ejecutar como script para que solo se ejecute esta funcion
if __name__ =='__main__':
    run()    
#llamamos a la funcion run() para que se ejecute

#la solicitud con fastapi, devuelve un array y un dict en la pagina web, pero tabien podemos hacer 
#que devuelva una pagina html viendo la documentacion de fastapi.escribimos response en 
#la pagina y escogemos custom response html
