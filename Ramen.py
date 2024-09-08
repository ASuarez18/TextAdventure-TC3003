import GlobalVars

def PuestoRamen(T):
    state = 0
    interrogate = False
    
    while state != 404:
        print("¡Bienvenido! a Kōdo Ramen. Pasa, resguardate del frio de la ciudad.")
        if state == 0:
            print("<Que desas hacer>")
            print("1. Hablar con el tendero")
            print("2. Salir del lugar")
            opt = input()
            if (opt == "1"):
                state = 1 # Hablar
            elif (opt == "2"):
                print("<Saliste del establecimiento>")
                return
            else:
                print("<Opcion invalida>")
        if state == 1:
            print("<Que deseas decirle al tendero>")
            print("1. Comprar")
            if (interrogate):
                print("2. Interrogar")
            if (GlobalVars.T):
                print("3. Inculpar")
            opt = input()
            if (opt == "1"):
                state = 2 # Comprar
            if (opt == "2" and interrogate):
                state = 3 # Interrogar
            if (opt == "3" and GlobalVars.T):
                state = 4 # Inculpar
            