from Lista import datos
from Lista import Lista_Datos

listar=Lista_Datos()

def nuevoContacto():
    print("Ingrese nombre:")
    nombre=input(">")
    print("Ingrese apellido")
    apellido=input(">")
    print("Ingrese numero de telefono")
    telefono=input(">")
    existe=listar.existe(telefono)
    while existe==True:
        print("Este numero ya existe, ingrese otro")
        print("Ingrese numero de telefono")
        telefono=input(">")
        existe=listar.existe(telefono)
    
    nuevo=datos(nombre,apellido,telefono)
    listar.agregar(nuevo)
    print("Contacto agregado satisfactoriamente")
    print("")
    
    
def buscarContacto():
    print("Ingrese numero para la busqueda")
    telefono=input(">")
    buscar=listar.buscar(telefono)
    if buscar==False:
        print("Contacto inexistente")
        print("¿Desea agregarlo? S/N")
        agre=input(">")
        if agre=="S" or agre=="s":
            nuevoContacto()

def agenda():
    listar.mostrarAgenda()
    
print("Bienvenido")
print("Seleccione la opción a realizar:")

op=0
try:
    while op!="4":
        
            print("1. Ingresar nuevo contacto")
            print("2. Buscar Contacto")
            print("3. Visualizar agenda")
            print("4. Salir")
            op=input(">")
            if op=="1":
                nuevoContacto()
            if op=="2":
                buscarContacto()
            if op=="3":
                agenda()
            
except Exception:
    print("Error")
    
print("Gracias, vuelve pronto")