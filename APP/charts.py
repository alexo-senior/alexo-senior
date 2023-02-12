import matplotlib.pyplot as plt

"""la libreria matplotlib primero se descarga en la terminal y luego se le agrega 
el punto pyplot, el alias es una practica comun para hacerlo mas resumido.Ahora vamos a 
generar unas lineas de codigo con una funcion para hacer una grafica
"""


def generate_bar_chart(name, labels, values):
    # AHORA FIG DE FIGURA Y AX DE COORDENADAS,LE PASAMOS EL METODO ALIAS PLT. SUBPLOTS()
    fig, ax = plt.subplots()
    # AX DE BAR PARA GRAFICAR, es decir los valores y los labels de esa grafica
    # enviamos los valores que son las variables labels y values
    ax.bar(labels, values)
    # ahora si lo graficamos
    plt.savefig(f'./{name}.png')
    plt.close()
    
def generate_pie_chart(labels, values):
    fig,ax = plt.subplots()
    ax.pie(values,labels == labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()
        
    #ahora ejecutamos commo un script par que solo se ejecute esa funcion que buscamos
if __name__ == '___main__':
    # llamamos a la funcion
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
    
            
            
        
        

    
    
    
        
        
    

