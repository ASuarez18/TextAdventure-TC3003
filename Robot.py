
import GlobalVars

def Robot():
    chat = True
    state = 0
    opciones = None
    #Create loop for a state machine
    while chat != False:
        if state == 0:
            print("Hola soy Robotronix , tu asistente virtual. ¿Necesitas informacion de algo en especifico?")
            print("1. Preguntarle al robot acerca de sitios turisticos")
            print("2. Preguntarle al robot acerca del horario del transporte")
            print("3. Interrogar al robot")
            print("4. Salir")
            opciones = int(input("Elije una opcion: "))
            if(opciones == 1):
                state = 1
            elif(opciones == 2):
                state = 2
            elif(opciones == 3):
                state = 3
            elif(opciones == 4):
                chat = False
            else:
                 print("Opcion invalida")
        if state == 1:
            print("Lo sitios turisticos mas cercanos de tu ubicacion actual son:")
            print(" Parque Nacional de Toluca")
            print(" Museo de Arte Moderna")
            print(" Teatro del Sol")
            print("0. Repetir opciones")
            print("1. Volver al menu principal")
            opciones = int(input("Elije una opcion: "))
            if(opciones == 0):
                state = 1
            elif(opciones == 1):
                state = 0
            else:
                 print("Opcion invalida")
        elif state == 2:
            print("El horario del transporte es:")
            print("Transporte Público:")
            print("De 6:00 AM a 10:00 AM")
            print("De 10:00 AM a 3:00 PM")
            print("De 3:00 PM a 6:00 PM")
            print("0. Repetir opciones")
            print("1. Volver al menu principal")
            opciones = int(input("Elije una opcion: "))
            if(opciones == 0):
                state = 2
            elif(opciones == 1):
                state = 0
            else:
                 print("Opcion invalida")
        elif state == 3:
             print("Para acceder a mi archivos nesecitas un codigo de seguridad")
             print("0.Dar codigo de seguridad")
             print("1. Volver al menu principal")
             opciones = int(input("Elije una opcion: "))
             if(opciones == 0):
                if(GlobalVars.E == True):
                    state = 4
                else:
                    print("No tienes el codigo de seguridad para acceder a mis archivos")
             elif(opciones == 1):
                 state = 0
             else:
                 print("Opcion invalida")                
        elif state == 4:
            print("Has accedido a tus archivos")
            print("¿Que archivos deseas?")
            print("1. Documentacion")
            print("2. Imagenes")
            print("3. Grabaciones")
            print("0. Volver al menu principal")
            opciones = int(input("Elije una opcion: "))
            if(opciones == 1):
                print("Has seleccionado la documentacion")
                print("Esta es la documentacion que contiene:")
                print("Documento 3X1736XAH")
                state = 4
            elif(opciones == 2):
                print("Has seleccionado las imagenes")
                print("Estas son las imagenes que contiene:")
                print("Imagen 1X3000XAH")
                print("Imagen 2X3000XAH")
                state = 4
            elif(opciones == 3):
                print("Has seleccionado las grabaciones")
                print("Las grabaciones estan es esta USB")
                GlobalVars.U = True
                state = 4
            elif(opciones == 0):
                state = 0

             

