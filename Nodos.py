
import enum
import random





class asiento:
    
    def __init__(self,ident,estado,posicion):
        
        self.ident     =    ident
        self.estado    =   estado
        self.posicion  = posicion
        self.size      =        0

    def setcosto(self,estado):
       
       if (self.estado == "Abatido" and estado == "Normal") or (self.estado == "Normal" and estado =="Abatido"):
            self.estado = estado
            return 2

       elif (self.estado == "Desplazado" and estado == "Normal") or (self.estado == "Normal" and estado == "Desplazado"):
            self.estado = estado
            return 1

        
       return 0 






class monovolumen:

    def __init__(self,sillon,espacio):

        self.sillon = sillon
        self.espacio = 200
    


    
    def calculo_espacio(self,sillones):
        
        self.espacio=200
        acumulador=0

        for asiento in sillones:
            if asiento.estado == "Desplazado":
                acumulador+=50
            elif asiento.estado == "Abatido":
                acumulador+=200 
    
        self.espacio+=acumulador
        
        return self.espacio



#codigo sacado de: https://github.com/joeyajames/Python/blob/master/LinkedLists/CircularLinkedList.py
# Nucleo
class Node(object):

    def __init__(self,costo,dato,n=None):
        self.costo=costo
        self.dato=dato
        self.next_node=n

    def get_next (self):
	    return self.next_node

    def set_next (self, n):
     	self.next_node = n
		
    def get_data (self):
    	return self.data

    def set_data (self, d):
       self.data = d
		


#inicializador pdta: hay que crear lo mas potente  .3. 
class ArbolBinario(object):

    def __init__(self,izquierda=None,derecha=None):
        
        self.izquierda = izquierda
        self.derecha   = derecha

    # el dato que sera llamado sera un tipo de dato lista , TENGAN MUCHO CUIDADO DE COLOCAR UN INTEGER/CHAR PORQUE LES DARA ERROR
    def add(self,dato):

        x1=0
        x2=1
        x3=2
        x4=3
        x5=4
        x6=5
        x7=6

        if self.izquierda == None :

          xi=random.randint(1,7)
          
          if xi == 2 and  dato[xi].estado=="Normal" and dato[x4].estado == "Abatido" and dato[x5].estado == "Abatido":

                valorcosto=dato[xi].setcosto("Desplazado")
                self.izquierda= Node(valorcosto,dato)   


        elif self.derecha == None :

            xi=random.randint(1,7)
          
            if xi == 2 and dato[x4].estado == "Abatido" and dato[x5].estado == "Abatido":

                valorcosto=dato[xi].setcosto("Abatido")
                self.derecha= Node(valorcosto,dato)



        
        

    

      

            
            

# Pueden Modificar Para que solo imprima el asiento pero si o si tiene que imprimir para el nodo
def loopescritura(Data):
    for asiento in Data:
        print(asiento.ident +" "+ asiento.estado +" "+ asiento.posicion)
    











