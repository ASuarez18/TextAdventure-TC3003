import GlobalVars
import Ramen
import Robot
import Inspeccionar
import Implante



# Función de calle en la que los posibles estados son:
# Puesto de ramen
# Robot
# Implantes
# Inspeccion
def Calle():
    print("Una noche más en la agitadas y luminosas calles de Tokio\
        tu trabajo como inspector privado no va muy bien ultimamente.....estas pensando en dejarlo\
        de pronto, tu celular suena....es la llamada de una madre desesperada por encontrar a su hija perdida\
        la ultima vez que supo de ella se encontraba en las calles de Akihabara, la madre te ha compartido la ultima ubicación\
        por lo que decides dirigirte a esta.\
        La victima depende de ti para ser encontrada, ¿Qué haras?\n")
    
    estado = 0
    while estado != 404:
        print("Opciones:\n")
        if(GlobalVars.InspCalle):
            print("1.- Entrar a tienda de Ramen.\
            2.- Hablar con Robot Asistente.\
            3.- Entrar a tienda de implantes tecnologicos.\
            4.- Inspeccionar calle.\n")
        else:
            print("1.- Entrar a tienda de Ramen.\
            2.- Hablar con Robot Asistente.\
            3.- Entrar a tienda de implantes tecnologicos.\n")
        
        opt = input()
        if(opt==1):
            Ramen.PuestoRamen()
        elif(opt==2):
            Robot.Robot()
        elif(opt==3):
            Implante.implante()
        elif(opt==4):
            Inspeccionar.Inspeccionar()
        else:
            print("Vaya, se que trabajar es dificil, pero hay que encontrar a la chica, vamos!\n")
    

Calle()