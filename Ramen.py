import GlobalVars

def PuestoRamen():
    state = 0
    interrogate = False
    print("¡Bienvenido! a Kōdo Ramen. Pasa, resguardate del frio de la ciudad.")

    while state != 404:
        if state == 0: # ! Llegada
            print("<Que desas hacer>")
            print("1. Hablar con el tendero")
            print("2. Salir del lugar")
            if(interrogate):
                print("3. Inculpar")
            opt = input("Elige una opcion: ")
            if (opt == "1"):
                state = 1 # ? Hablar
            elif (opt == "2"):
                state = 400 # ? Despedida
            else:
                print("<Opcion invalida>")
        
        elif state == 1: # ! Hablar
            print("<Que deseas decirle al tendero?>")
            print("1. Comprar")
            print("2.Salir")
            if (interrogate):
                print("3. Interrogar")
            if (GlobalVars.T):
                print("4. Inculpar")
            opt = input()
            if (opt == "1"):
                state = 2 # ? Comprar
            elif (opt == "2"):
                state = 400 # ? Despedida
            elif (opt == "3" and interrogate):
                state = 3 # ? Interrogar
            elif (opt == "4" and GlobalVars.T):
                state = 4 # ? Inculpar
            else:
                print("<Opcion invalida>")
        
        elif state == 2: # ! Comprar
            print("<Que deseas comprar?>")
            print("1. Sake")
            print("2. Ramen")
            print("3. Salir")
            opt = input()
            if (opt == "1"):
                print("<Le das un trago al sake y te relajas un poco>")
                interrogate = True
                state = 1 # ? Hablar
            elif (opt == "2"):
                print("<El comer ramen calienta un poco tu cuerpo>")
                interrogate == True
                state = 1 # ? Hablar
            elif (opt == "3"):
                state = 1 # ? Hablar
            else:
                print("<Opcion invalida>")

        elif state == 3: # ! Interrogar
            print("<Comienzas a interrogar al tendero>")
            print("El tendero te menciona sobre una chica que entro un poco agitada, no pidio nada, estuvo como unos 5 minutos. Salio corriendo dejando atras un telefono.")
            print("<Tomas el celular>")
            GlobalVars.T = True
            print("<Celular añadido a inventario>")
            state = 1 # ? Hablar

        elif state == 4: # ! Inculpar
            print("<Estas seguro de que deseas inculpar al tendero>")
            print("1. Si\n2.No")
            opt = input()
            if (opt == "1"):
                print("<Inculpaste al tendero>")
                state = 404 # ? Fin
            elif (opt == "2"):
                print("<Regresas a hablar con el tendero>")
                state = 1 # ? Hablar
            else:
                print("<Opcion invalida>")
        
        elif state == 400:
            print("<Saliste del establecimiento>")
            state = 404
        
        else:
            return
    return


PuestoRamen()
