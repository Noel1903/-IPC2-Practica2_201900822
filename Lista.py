import os

class datos:
    def __init__(self,nombre=None,apellido=None,telefono=None):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        
class Nodo:
    def __init__(self,datos=None,siguiente=None,anterior=None):
        self.datos=datos
        self.siguitente=siguiente
        self.anterior=anterior
        
        
class Lista_Datos:
    def __init__(self,cabeceraR=None,registro=None):
        self.cabeceraR=cabeceraR
        self.registro=registro
        self.tamaño=0
        
    def agregar(self,datos):
        nuevo_nodo=Nodo(datos)
        if self.tamaño==0:
            self.cabeceraR=nuevo_nodo
            self.registro=nuevo_nodo
        else:
            self.registro.siguitente=nuevo_nodo
            nuevo_nodo.anterior=self.registro
            self.registro=nuevo_nodo
            
        self.tamaño+=1
        
    def buscar(self,telefono):
        nodo=self.cabeceraR
        encontrado=False
        while nodo!=None:
            if telefono==nodo.datos.telefono:
                print("Nombre: ",nodo.datos.nombre)
                print("Apellido: ",nodo.datos.apellido)
                print("Número teléfonico: ",nodo.datos.telefono)
                break                
            nodo=nodo.siguitente
            
        if nodo==None:
            return False
        
        
    def existe(self,telefono):
        nodo=self.cabeceraR
        while nodo!=None:
            if telefono==nodo.datos.telefono:
                return True              
            nodo=nodo.siguitente
            
    def mostrarAgenda(self):
        partes=""
        nodo=self.cabeceraR
        contador=1
        while nodo!=None:
            partes+=str(contador)+"[label=\" Nombre: "+nodo.datos.nombre+"\nApellido: "+nodo.datos.apellido+"\nTelefono: "+nodo.datos.telefono+"\" shape=square];\n"
            contador+=1
            nodo=nodo.siguitente
            
        for i in range(1,self.tamaño):
            partes+=str(i)+"->"+str(i+1)+";\n"
            partes+=str(i+1)+"->"+str(i)+";\n"
            
        grafica="digraph G{agenda->1;\n"+partes+"}"
        documento=open("Agenda.dot","w",encoding="utf-8")
        documento.write(grafica)
        documento.close()
        os.system("dot.exe -Tpng Agenda.dot -o Agenda.png")
        os.startfile("Agenda.png")
        
        