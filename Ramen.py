import GlobalVars

def PuestoRamen():
    state = 0
    interrogate = False
    while state != 404:
        print("¡Bienvenido! a Kōdo Ramen. Pasa, resguardate del frio de la ciudad.")
        if state == 0:
            print("<Que deseas hacer>")
            print("1. Hablar con el tendero")
            print("2. Salir del lugar")
            if(interrogate):
                print("3. Inculpar")
            opt = input("Elige una opcion: ")
            if (opt == "1"):
                state = 1 # Hablar
                GlobalVars.PuntajeActual += 1
            elif (opt == "2"):
                print("<Saliste del establecimiento>")
                GlobalVars.PuntajeActual += 1
                return
            elif (opt == "3"):
                GlobalVars.PuntajeActual += 1
                state = 6
            else:
                print("<Opcion invalida>")
        #Menu principal
        if state == 1:
            print("Tendero: Hola, ¿en qué puedo ayudarte?")
            print("1. Preguntar sobre la chica desparecida")
            print("2. Comprar")
            print("3. Decir que su comida es mala")
            print("4. Salir del lugar")
            opt = input("Elige una opcion: " )
            if(opt == "1"):
                print("No se de que me estas hablando")
                GlobalVars.PuntajeActual += 1
                state = 1
            elif(opt == "2"):
                GlobalVars.PuntajeActual += 1
                state = 2
            elif (opt == "3"):
                print("Tonterias, te puedes ir a la mierda")
                GlobalVars.PuntajeActual += 1
                state = 1
            elif (opt == "4"):
                print("<Saliste del establecimiento>")
                GlobalVars.PuntajeActual += 1
                GlobalVars.InspCalle = True
                return
            else:
                print("<Opcion invalida>")
        #Estado de compra
        if(state == 2):
            print("Tendero: ¿Cuál producto deseas comprar?")
            print("1. Ramen")
            print("2. Sake")
            print("3. Volver al menu")
            opt = input("Elige una opcion: ")
            if (opt == "1"):
                print("Compraste un ramen")
                if(interrogate):
                    state = 7
                GlobalVars.PuntajeActual += 1
                state = 3
            elif (opt == "2"):
                print("Compraste un sake")
                if(interrogate):
                    state = 7
                GlobalVars.PuntajeActual += 1
                state = 3
            elif (opt == "3"):
                print("<Regresaste al menu>")
                GlobalVars.PuntajeActual += 1
                state = 1
            else:
                print("<Opcion invalida>")
        #Conversacion
        if(state == 3):
            print("Tendero: Ahora que lo veo , no eres de por aqui o si?\
                  Estas detras de alguien , tal vez recuperar a alguien o me equivoco jajaja.\
                  Era broma no te pongas asi, veras hace tres dias una chica con pelo corto con un unicornio de papel\
                  paso por estos rumbos.")
            print("1. Preguntar acerca de la chica")
            print("2. Comentarle que no es asunto de el")
            print("3.Volver al menu")
            opt = input("Elige una opcion: ")
            if (opt == "1"):
                GlobalVars.PuntajeActual += 1
                state = 4
            elif (opt == "2"):
                GlobalVars.PuntajeActual += 1
                state = 5
            elif (opt == "3"):
                GlobalVars.PuntajeActual += 1
                print("<Regresaste al menu>")
                state = 1
            else:
                print("<Opcion invalida>")
        #Estado de encontrar telefono (Pista Principal)
        if(state == 4):
            print("Tendero: El ultimo rastro que se de la chica es este telefono viejo.\
                  Lo dejo aca tirado luego de probar mis deliciosos platillos.\
                  No te voy a mentir, esa chica la verdad era bastante guapa jajajaja\
                  Es una lastima que se haya extraviado por lo que puedo dar cuenta.\
                  Ten , este telefono te sirve mas a ti que a mi. Avisame si la encuentras, aunque lo dude mucho.")
            print("<Recibiste un telefono celular en malas condiciones>")
            GlobalVars.T = True
            GlobalVars.InspCalle = True
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
                print("<Opcion invalida>")
        #Estado final de compra
        if(state == 7):
            print("Gracias por comprar espero que lo disfrutes!")
            return
        #Seleccion de inculpar confirmada
        if(state == 7):
            #Acabar la historia luego de inculpar al tendero por el crimen
            return
