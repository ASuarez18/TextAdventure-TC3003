import GlobalVars

def Mejora():
    print("Cirujano: Hola veo que te interesa estos implantes, son de lo mejor que hay en el mercado")
    print("Cirujano: Tengo varios modelos, cual te gustaria ver?")
    print("1. Implante de ojos")
    print("2. Implante de olfato")
    print("3. salir")
    
    
    if(GlobalVars.T and GlobalVars.U and GlobalVars.C):
        print("4. Inculpar al cirujano")
    
    opciones = int(input("Que deseas hacer? "))
    if(opciones == 1):
        print("Cirujano: En un momento te lo pongo")
        print("tin tin tin")
        print("Cirujano: Listo, ya esta puesto")
        GlobalVars.inventario.append("Implante de ojos")
        return False  
    elif(opciones == 2):
        print("Cirujano: En un momento te lo pongo")
        print("tin tin tin")
        print("Cirujano: Listo, ya esta puesto")
        GlobalVars.inventario.append("Implante de olfato")
        return False  
    elif(opciones == 4):
        print("Cirujano: Todo bien chico, porque me ves tan raro?")
        print("No se, es que me parece raro que tengas tantos implantes y te veas tan normal tas el desaparecimiento de la chica")
        print("Cirujano: No se de que me hablas, yo no tengo nada que ver con eso")
        print("Enserio? Porque no me parece que sea asi")
        print("Cirujano: ejem, ejem, bueno, me tengo que ir, tengo cosas que hacer")
        print("No te vayas, tengo que hablar contigo")
        print("tengo varias cosas que me dicen que tu tienes algo que ver con la desaparicion de la chica")
        print("Cirujano: Como sabes eso?, si hice todo lo posible para que no se supiera")
        print("Cirujano: No importa, si te elimino, no habra problema")
        print("<Saco rapidamente mi arma y le disparo al cirujano>")
        print("El cirujano cae al suelo muerto")
        print("<Veo que tenia un papel en su bolsillo>")
        print("<Lo abro y decia: 'Codigo de la puerta 1234'>")
        print("<Tomo el papel y me voy de la habitacion detras de la puerta>")
        print("<Abro la puerta y veo a la chica amarrada>")
        print("<La desamarrro y la llevo a la salida>")
        print("FIN")

        return True


    else:
        print("No te interesa nada? Bueno, como quieras")
        return False  


def implante():

    estado = 0 
    salidad= False
    opcion = 0
    while(salidad == False):
        print("Vaya hay varias cosas en las cuales estan en venta \n pero sin ninguna pista que me puede dar una idea de donde esta la chica")
        print("\n<Se ve interesante estos implantes, que deberia hacer? >\n")
        print("1. Hablar con el cirujano")
        print("2. Seguir buscando")
        print("3. Salir del lugar")
        estado = int(input())
        if(estado == 1):
            salidad = Mejora()

        elif(estado == 2):
            print("<Veo un dinero en el suelo>")
            print("<Ademas de ver un terminal para envia mensajes>")
            print("1. Tomar el dinero")
            print("2. ir a ver la terminal")
            print("3. Regresar")
            opcion = int(input("Que deseas hacer?"))
            if(opcion == 1):
                print("Tomo el dinero")
                GlobalVars.inventario.append("Dinero")
            elif(opcion == 2):
                print("Veo que el terminal esta bloqueado")
                print("Parece necesitar un codigo para desbloquearlo")
                print("Voy a ver si puedo encontrar algo que me ayude a desbloquearlo")
            elif(opcion == 3):
                print("<Vuelvo a la entrada>")

        elif(estado == 3):
            print("No me interesa nada de esto, mejor me voy")
            return None
        
        else:
            print("Oye, apresurate que tengo cosas que hacer")
            print("Si dejame seguir viendo que hacer")