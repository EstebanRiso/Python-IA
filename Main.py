from Nodos import monovolumen, asiento, loopescritura, Node, ArbolBinario




def crear_datos(data):

    a="Abatido"
    b="Normal"



    # Nuestra DATA *NO MODIFICAR
    # su funcionamiento es igual al arraylist de java ( osea se puede colocar cualquier cosa)
    # lo hice asi porque me dio un poco de flojera escribir el add en la clase "asiento" y tambien porque no era 
    # necesario debido a que no es algo que
    # voy a crear de manera constante sino mas bien es algo fijo.
    

    data.append( asiento("X1",b,"Chofer"))
    data.append( asiento("X2",b,"Copiloto"))
    data.append( asiento("X3",b,"Segunda_Fila-Izquierda_Ventana"))
    data.append( asiento("X4",b,"Segunda_Fila-Centro"))
    data.append( asiento("X5",b,"Segunda_Fila-Derecha-Ventana"))
    data.append( asiento("X6",a,"Tercera_Fila-Izquierda"))
    data.append( asiento("X7",a,"Tercera_Fila-Derecha"))


    loopescritura(data)
    
    return data


def crear_meta(data):
    
    a="Abatido"
    b="Normal"

    data.append( asiento("X1",b,"Chofer"))
    data.append( asiento("X2",b,"Copiloto"))
    data.append( asiento("X3",b,"Segunda_Fila-Izquierda_Ventana"))
    data.append( asiento("X4",a,"Segunda_Fila-Centro"))
    data.append( asiento("X5",b,"Segunda_Fila-Derecha-Ventana"))
    data.append( asiento("X6",b,"Tercera_Fila-Izquierda"))
    data.append( asiento("X7",b,"Tercera_Fila-Derecha"))

    return data



#declaracion de nuestro principal

def main():

    Asientos= []
    Asientos= crear_datos(Asientos)
    Estados_meta=[]
    Estados_meta=crear_meta(Estados_meta)
    



# aqui empieza y muere la magia :V
main()




