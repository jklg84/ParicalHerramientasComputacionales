#ES NECESARIO INSTALAR ALGUNAS LIBRERIAE EN CONSOLA, REVISAR LOS LINKS

#Importamos librerias para acceso a datos en archivos 
import json


#Importamos librerias para hacer print de colores
from colorama import Fore, Back, Style
#https://pypi.org/project/colorama/


#Definir ruta de los archivos
ruta_productos = "productos.json"#ruta de usuarios


##############################################################################
##########################    FUNCIONES     ##################################
##############################################################################

def bienvenida():

    print("\n#######################################")
    print(Back.BLUE, "sistema de descuentos de la cafeteria", Back.RESET)
    print("#######################################")
    print("\n1. Registrar producto",
          "\n2. Usar servicio",
          "\n3. Salir")
    opcion = eval(input("\nElija una opción: "))
    
    if opcion == 1:
        registro()
        
    elif opcion == 2:
        usar_servicio()
        
    elif opcion == 3:
        chao = True
        return chao
        
    else:
        return
##############################################################################
##############################################################################    


def registro():
    
    print("\n\n###################################")
    print(Back.YELLOW,"Bienvenido al sistema de Registro",Back.RESET)
    print("##################################")
    
    datos = archivo_productos_r()

    ingreso = solicitud_datos() 
    
    #Verificacion si producto ya esta registrado    
    for x in range(len(datos['productos'])):

        if(datos['productos'][x][1]==ingreso[1]):

            print("\n\n#########################################################",
                  "\nEl codigo de producto ya esta en la base de datos",
                  "\nPuede usar la opcion de alterar o borra")
            return
               
    datos['productos'].append(ingreso)
    archivo_productos_w(datos)
    print("\n\nProducto registrado con exito!")
    return
    

##############################################################################
##############################################################################
  
def usar_servicio():

    print("\n\n#####################################")
    print(Back.CYAN,"Bienvenido al sistema de desarrollo",Back.RESET)
    print("#####################################")
    
    datos = archivo_productos_r()

    identificacion = int(input("Digite la Identificacion del usuario: "))
    print()
    
    print('Rol del usuario'
          '\n'
          '\n1.Estudiante'
          '\n2.Profesor')
    rol = int(input("opcion: "))
    if rol == 1:
        rol="Estudiante"
    elif rol == 2:
        rol = "Profesor"
    else:
        bienvenida()
        
    producto = int(input("Digite el codigo del producto: "))
       
    for x in range(len(datos['productos'])):
        
        if(datos['productos'][x][0]==producto):
            resultado = datos['productos'][x][1]*datos['productos'][x][2]
            if rol == "Estudiante":
                porcentaje = resultado*0.50
                total = resultado - porcentaje
            elif rol == "Profesor":
                porcentaje = resultado*0.20
                total = resultado - porcentaje
                
            print()
            print(f'El usuario de identificacion {identificacion} debe pagar {total}$ por el producto {producto}')

            break 
             
##############################################################################
##############################################################################

def solicitud_datos():
    codigo = int(input("Digite el codigo de producto: "))

    cantidad = int(input("Digite la cantidad de unidades: "))

    precio = int(input("Digite el precio del producto: "))


    ingreso = [codigo, cantidad, precio]
    return ingreso
        
##############################################################################
####################   PROCESANDO ARCHIVOS   #################################
##############################################################################
    
def archivo_productos_r():
    #Inicializacion de diccionarios
    datos = {}
    datos['productos'] = []

    #comando para verificar si el arcivo existe y tiene valores   
    try:
        with open (ruta_productos,'r', encoding="utf-8") as file:
            datos = json.load(file)
        return datos
    except:
        print(f"la Base de datos {ruta_productos} no ha sido encontrada")
        return datos #si no hay datos significa que no hay nada es decir retorna el diccionario vacia 

#Escrita del archivo JSON
def archivo_productos_w(datos):
    try:
        with open(ruta_productos, 'w', encoding="utf-8") as file:
            json.dump(datos, file)
            return
    except:
        print(f"la Base de datos {ruta_productos} no ha sido encontrada")
        
##############################################################################
##############################     MAIN     ##################################
##############################################################################
salir = "no"

while(salir=="no"):
    chao = bienvenida()
    if(chao==True):
        break
    else:
        salir="no"
print()
print(Back.GREEN, "Gracias por utilizar el sistema", Back.RESET)

