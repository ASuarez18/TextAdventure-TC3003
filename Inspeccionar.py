import GlobalVars

# Definición del estado de inspección como variable global
estado_inspeccion = 0

# Función que permite inspeccionar la calle
def Inspeccionar():
    global estado_inspeccion

    if estado_inspeccion == 0:
        print("<Encontraste un Unicornio de Papel>")
        print("<Parece que alguien lo dejó por accidente. Pero está bonito>")

        # Se agrega el objeto al inventario
        GlobalVars.P = True
        estado_inspeccion = 1

    elif estado_inspeccion == 1:
        print("<Encontraste una Envoltura de Dulce.>")
        print("<Está un poco arrugada y sucia, pero parece que tiene un código.>")

        # Se agrega el objeto al inventario
        GlobalVars.E = True
        estado_inspeccion = 2

    else:
        print("<Decidiste terminar la inspección.>")
        print("<No parece haber nada más de interés por aquí.>")