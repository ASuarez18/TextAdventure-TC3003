import GlobalVars

def Mejora():
    print("Hola veo que te interesa estos implantes, son de lo mejor que hay en el mercado")
    print("Tengo varios modelos, cual te gustaria ver?")
    print("1. Implante de ojos")
    print("2. Implante de olfato")
    print("3. salir")
    
    if(GlobalVars.T and GlobalVars.U and GlobalVars.C):
        print("4. Inculpar al cirujano")
    print("Entonces, cual te gustaria que te ponga?")
    opciones = int(input())
    if(opciones == 1):
        print("En un momento te lo pongo")
        print("tin tin tin")
        print("Listo, ya esta puesto")
        GlobalVars.inventario.append("Implante de ojos")
    elif(opciones == 2):
        print("En un momento te lo pongo")
        print("tin tin tin")
        print("Listo, ya esta puesto")
        GlobalVars.inventario.append("Implante de olfato")
    elif(opciones == 4):
        print("Todo bien chico, porque me ves tan raro?")
        print("No se, es que me parece raro que tengas tantos implantes y te veas tan normal tas el desaparecimiento de la chica")
        print("No se de que me hablas, yo no tengo nada que ver con eso")
        print("Enserio? Porque no me parece que sea asi")
        print("ejem, ejem, bueno, me tengo que ir, tengo cosas que hacer")
        print("No te vayas, tengo que hablar contigo")
        print("tengo varias cosas que me dicen que tu tienes algo que ver con la desaparicion de la chica")
        print("Como sabes eso?, si hice todo lo posible para que no se supiera")
        print("No importa, si te elimino, no habra problema")
        print("Saco rapidamente mi arma y le disparo al cirujano")
        print("El cirujano cae al suelo muerto")
        print("Veo que tenia un papel en su bolsillo")
        print("Lo abro y decia: 'Codigo de la puerta 1234'")
        print("Tomo el papel y me voy de la habitacion detras de la puerta")
        print("Abro la puerta y veo a la chica amarrada")
        print("La desamarrro y la llevo a la salida")
        print("FIN")


    else:
        print("No te interesa nada? Bueno, como quieras")    


def implante():

    estado = 0 
    salidad= False
    opciones = 0
    while(salidad == False):
        print("Vaya hay varias cosas en las cuales estan en venta \n pero sin ninguna pista que me puede dar una idea de donde esta la chica")
        print("\n Se ve interesante estos implantes, que deberia hacer? \n")
        print("1. Hablar con el cirujano")
        print("2. Seguir buscando")
        print("3. Salir del lugar")
        estado = int(input())
        if(estado == 1):
            print("Hola veo que te interesa estos implantes, son de lo mejor que hay en el mercado")
            print("Tengo varios modelos, cual te gustaria ver?")
            print("1. Implante de ojos")
            print("2. Implante de olfato")
            print("3. salir")
            print("Entonces, cual te gustaria que te ponga?")
            opciones = int(input())
            if(opciones == 1):
                print("En un momento te lo pongo")
                print("tin tin tin")
                print("Listo, ya esta puesto")
                GlobalVars.inventario.append("Implante de ojos")
            elif(opciones == 2):
                print("En un momento te lo pongo")
                print("tin tin tin")
                print("Listo, ya esta puesto")
                GlobalVars.inventario.append("Implante de olfato")
            else:
                print("No te interesa nada? Bueno, como quieras")

        elif(estado == 2):
            print("Oye, apresurae que tengo cosas que hacer")
            print("Si dejame seguir viendo que hacer")
        elif(estado == 3):
            print("No me interesa nada de esto, mejor me voy")
            return None
        
        else:
            print("Oye, apresurae que tengo cosas que hacer")
            print("Si dejame seguir viendo que hacer")