#PRIMERO IMPORTAMOS EL MODULO CSV PARA TRABAJAR CON ESTE TIPO DE ARCHIVO

import csv

"""DEFINIMOS UNA FUNCION LE PASAMOS EL PARAMETRO PATH (UBICACION),LUEGO USAMOS LA 
SINTAXIS (with open) PARA ABRIR EL ARCHIVO Y QUE SE CIERRE AUTOMATICAMENTE, LE PASAMOS 
LA UBICACION (EL NOMBRE DEL PARAMETRO DE LA FUNCION,Y LA R DE LECTURA SI ESO 
ES LO QUE QUEREMOS ENTRE COMILLAS, EL ALIAS AS,Y le ponemos CSVFILE, LUEGO CREAMOS UNA
VARIABLE LE ASIGNAMOS EL NOMBRE DEL MODULO CSV PUNTO READER, PARENTESIS EL NOMBRE
DEL ARHIVO CSVFILE(alias) COMA EL METODO DELIMITER QUE SE ENCARGARA DE HACER LA SEPARACION
DEL TEXTO DEL ARCHIVO CSV, YA SEA POR COMAS O POR PUNTO Y COMA, ESO LO DEBEMOS MIRAR
ANTES LUEGO DE DESCARGAR EL ARCHIVO CSV """


def read_csv(path):
    with open(path, 'r',) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        # para obtener array con los nombres de las columnas(prim fila)
        data = []
        # print(header)
        for row in reader:
            # print(row)
            iterable = zip(header, row)
            #print(list(iterable))
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
            return data
            #print(country_dict)
    
if __name__ == '__main__':
    data = read_csv('C:/Users/Alexis/Documents/EJERCICIOS PROG.Y PDF/RUTA PLATZI/APP/data.csv')
    print(data[0])
#ahora vamos a utilizar un zip para unir dos archivos el header con el row, es decir las
#las columnas y las filas.
            
    
    
        
"""la sintaxis siguiente es para que se ejecute solo el codigo del archivo actual,
en caso que tengamos modulos con mas de una funcion y queremos que se ejecute solo
un archivo en especifico"""

#de esta forma se puede ver solo como un array, sin embargo es mejor quede en formato
#de diccionario.
#de esa forma nos arroja una lista con tuplas, pero necesitamos un dict aplicamos la
#sintaxis de comprehension








    
