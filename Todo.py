# Evidencias
T = False
U = False
C = False
E = False
P = False

# Variables Ramen
InterrRamen = False

# Variables Calle
InspCalle = False

# Variables Robot
Codigo = False

#Punatje
puntuajeActual = 0

sumPuntuaje = 0

#Inventario
inventario = []

#Zona de ramen

def PuestoRamen():
    global puntuajeActual
    global inventario
    global T
    global InterrRamen




    state = 0
    interrogate = False
    while state != 404:
        print("¡Bienvenido! a Kōdo Ramen. Pasa, resguardate del frío de la ciudad.")
        if state == 0:
            print("<Que deseas hacer>")
            print("1. Hablar con el tendero")
            print("2. Salir del lugar")
            if(interrogate):
                print("3. Inculpar")
            opt = input("Elige una opcion: ")
            if (opt == "1"):
                state = 1 # Hablar
                puntuajeActual = puntuajeActual + 1
            elif (opt == "2"):
                print("<Saliste del establecimiento>")
                puntuajeActual = puntuajeActual + 1
                return
            elif (opt == "3"):
                puntuajeActual = puntuajeActual + 1
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
                puntuajeActual = puntuajeActual + 1
                state = 1
            elif(opt == "2"):
                puntuajeActual = puntuajeActual + 1
                state = 2
            elif (opt == "3"):
                print("Tonterias, te puedes ir a la mierda")
                puntuajeActual = puntuajeActual + 1
                state = 1
            elif (opt == "4"):
                print("<Saliste del establecimiento>")
                puntuajeActual = 1
                InspCalle = True
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
                puntuajeActual = puntuajeActual + 1
                state = 3
            elif (opt == "2"):
                print("Compraste un sake")
                if(interrogate):
                    state = 7
                puntuajeActual = puntuajeActual + 1
                state = 3
            elif (opt == "3"):
                print("<Regresaste al menu>")
                puntuajeActual += 1
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
                puntuajeActual = puntuajeActual + 1
                state = 4
            elif (opt == "2"):
                puntuajeActual = puntuajeActual + 1
                state = 5
            elif (opt == "3"):
                puntuajeActual = puntuajeActual + 1
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
            T = True
            InspCalle = True
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
                puntuajeActual = puntuajeActual + 1
                state = 8
            elif (opt == "2"):
                print("<Regresaste al menu>")
                puntuajeActual = puntuajeActual + 1
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
        
#Zona de Robot
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
                if(E == True):
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
                U = True
                state = 4
            elif(opciones == 0):
                state = 0

#Zona de Implante
def Mejora():
    global T
    global U
    global P
    global inventario

    print("Cirujano: Hola veo que te interesa estos implantes, son de lo mejor que hay en el mercado")
    print("Cirujano: Tengo varios modelos, cual te gustaria ver?")
    print("1. Implante de ojos")
    print("2. Implante de olfato")
    print("3. salir")
    
    
    if(T and U and P):
        print("4. Inculpar al cirujano")
    
    opciones = int(input("Que deseas hacer? "))
    if(opciones == 1):
        print("Cirujano: En un momento te lo pongo")
        print("tin tin tin")
        print("Cirujano: Listo, ya esta puesto")
        inventario.append("Implante de ojos")
        return False  
    elif(opciones == 2):
        print("Cirujano: En un momento te lo pongo")
        print("tin tin tin")
        print("Cirujano: Listo, ya esta puesto")
        inventario.append("Implante de olfato")
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
                inventario.append("Dinero")
            elif(opcion == 2):
                print("Veo que el terminal esta bloqueado")
                print("Parece necesitar un codigo para desbloquearlo")
                print("Voy a ver si puedo encontrar algo que me ayude a desbloquearlo")
            elif(opcion == 3):
                print("<Vuelvo a la entrada>")

        elif(estado == 3):
            print("No me interesa nada de esto, mejor me voy")
            InspCalle = True
            return None
        
        else:
            print("Oye, apresurate que tengo cosas que hacer")
            print("Si dejame seguir viendo que hacer")

#Zona de Inspeccionar calle
# Definición del estado de inspección como variable global
estado_inspeccion = 0

# Función que permite inspeccionar la calle
def Inspeccionar():
    global estado_inspeccion
    global P
    global E

    if estado_inspeccion == 0:
        print("<Encontraste un Unicornio de Papel>")
        print("<Parece que alguien lo dejó por accidente. Pero está bonito>\n")

        # Se agrega el objeto al inventario
        P = True
        estado_inspeccion = 1

    elif estado_inspeccion == 1:
        print("<Encontraste una Envoltura de Dulce.>")
        print("<Está un poco arrugada y sucia, pero parece que tiene un código.>\n")

        # Se agrega el objeto al inventario
        E = True
        estado_inspeccion = 2

    else:
        print("<Ya no hay nada más que inspeccionar.>")
        print("<No parece haber nada más de interés por aquí.>\n")


# Función de calle en la que los posibles estados son:
# Puesto de ramen
# Robot
# Implantes
# Inspeccion
def Calle():
    print("Una noche más en la agitadas y luminosas calles de Tokio\
        \ntu trabajo como inspector privado no va muy bien ultimamente.....estas pensando en dejarlo\
        \nde pronto, tu celular suena....es la llamada de una madre desesperada por encontrar a su hija perdida\
        \nla ultima vez que supo de ella se encontraba en las calles de Akihabara, la madre te ha compartido la ultima ubicación\
        \npor lo que decides dirigirte a esta.\
        \nLa victima depende de ti para ser encontrada, ¿Qué haras?\n")
    
    estado = 0
    while estado != 404:
        print("Opciones:\n")
        print("1.- Entrar a tienda de Ramen.\
        \n2.- Hablar con Robot Asistente.\
        \n3.- Entrar a tienda de implantes tecnologicos.\
        \n4.- Inspeccionar calle.\n")
        
        
        opt = int(input())
        if(opt==1):
            PuestoRamen()
        elif(opt==2):
            Robot()
        elif(opt==3):
            implante()
        elif(opt==4):
            Inspeccionar()
        else:
            print("Vaya, se que trabajar es dificil, pero hay que encontrar a la chica, vamos!\n")
    

Calle()