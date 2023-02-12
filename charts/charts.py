import matplotlib.pyplot as plt

def generate_pie_charts():
    labels = ['A','B','C']
    values = [200,34,120]
    
    
    fig, ax = plt.subplots()
    ax.pie(values,labels = labels)
    #ahora generamos una imageme en vez de una grafica para que el programa no se detenga
    #poor eso en vez de eusar show(), usamos savefig para guardarlo
    plt.savefig('pie.png')
    plt.close()
    


