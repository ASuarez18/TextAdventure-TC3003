import GlobalVars

def PuestoRamen():
    state = 0
    interrogate = False
    print("Tendero: ¡Bienvenido a Kōdo Ramen! Pasa, resguárdate del frío de la ciudad.")

    while state != 404:
        if state == 0:  # ! Llegada
            print("\n¿Qué deseas hacer?")
            print("1. Hablar con el tendero")
            print("2. Salir del lugar")
            if interrogate:
                print("3. Inculpar")
            opt = input("Elige una opción: ")
            if opt == "1":
                state = 1  # ? Hablar
            elif opt == "2":
                state = 400  # ? Despedida
            else:
                print("Opción inválida.")
        
        elif state == 1:  # ! Hablar
            print("\nTendero: ¿En qué puedo ayudarte?")
            print("1. Comprar")
            print("2. Salir")
            if interrogate:
                print("3. Interrogar")
            if GlobalVars.T:
                print("4. Inculpar")
            opt = input("Elige una opción: ")
            if opt == "1":
                state = 2  # ? Comprar
            elif opt == "2":
                state = 400  # ? Despedida
            elif opt == "3" and interrogate:
                state = 3  # ? Interrogar
            elif opt == "4" and GlobalVars.T:
                state = 4  # ? Inculpar
            else:
                print("Opción inválida.")
        
        elif state == 2:  # ! Comprar
            print("\nTendero: ¿Qué deseas comprar?")
            print("1. Sake")
            print("2. Ramen")
            print("3. Salir")
            opt = input("Elige una opción: ")
            if opt == "1":
                print("Bebes un trago de sake y te relajas un poco.")
                interrogate = True
                state = 1  # ? Hablar
            elif opt == "2":
                print("El ramen caliente reconforta tu cuerpo.")
                interrogate = True
                state = 1  # ? Hablar
            elif opt == "3":
                state = 1  # ? Hablar
            else:
                print("Opción inválida.")
        
        elif state == 3:  # ! Interrogar
            print("\nComienzas a interrogar al tendero.")
            print("Tendero: Una chica entró muy agitada, no pidió nada y se fue rápido, dejando un teléfono atrás.")
            print("Has añadido un teléfono a tu inventario.")
            GlobalVars.T = True
            return
        #Interrogar
        if(state == 5):
           print("Vaya no te tienes que poner en ese estado, solo trataba de ayudar imbecil")
           state = 1
        if(state == 6):
            print("Tendero: Que crees que haces puñetas? No sabes con quien te metes")
            print("1. Confirmar")
            print("2. Cancelar")
            opt = input("Elige una opcion: ")
            if (opt == "1"):
                GlobalVars.PuntajeActual += 1
                state = 8
            elif (opt == "2"):
                print("<Regresaste al menu>")
                GlobalVars.PuntajeActual += 1
                state = 1
            else:
                print("Opción inválida.")
        
        elif state == 400:
            print("Has salido del establecimiento.")
            state = 404
        
        else:
            return

    return

PuestoRamen()
