import charts
"""importamos el modulo creado creamos una funcion la llamamos run, luego 
el nombre del modulo punto llamando  a la funcion.
como queremos que se ejecute como un script, escribimos la sintaxis para esto"""

def run():
    charts.generate_pie_charts()
    

if __name__ =='__main__':
    run()
    #colocando el run()le decimos que cuando se ejecute como un script corra la funcion run
    