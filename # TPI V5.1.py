import os

while True:
    print("➖" * 70)
    print(f"Estimado cliente usted se encuentra en el sistema para calcular con exactitud el material utilizado en su proxima obra.\n")
    while True : 
        cliente = input("👷 Ingrese su nombre para poder cargarlo en nuestro sistema: ").upper()
        if len(cliente) > 3:
            break
        print("❌ Asegurese de ingresar un nombre valido ! ❌\n\n")

    while True :
        apellido = input("👷 Ingrese su apellido para poder cargarlo en nuestro sistema: ").upper()
        if len(apellido) > 3:
            break
        print("❌ Asegurese de ingresar un apellido valido ! ❌\n\n")

    while True : # Valida el ingreso del DNI
        dni = int(input("👷 Ingrese su DNI para poder cargarlo en nuestro sistema: "))
        if len(str(dni)) > 5:
            break
        print("❌ Asegurese de ingresar un numero de documento valido ! ❌\n\n")

    while True : # Valida el ingreso del Telefono
        telefono = int(input("👷 Ingrese su numero telefonico para poder cargarlo en nuestro sistema: "))
        if len(str(telefono)) > 9:
            break
        print("❌ Asegurese de ingresar un numero de telefono valido ! ❌\n\n")

    print("➖" * 70)
    while True:  # Valida la entrada de la unidad de Medida.
        try:
            unidad = float(input(f"Seleccione la unidad de medida que va a utilizar: \n\t\t1 - Metros.\n\t\t2 - Centimetros.\n\t\t3 - Pies.\n\n> > > "))
            if unidad == 1 or unidad == 2 or unidad ==3  :
                break
            print("❌ Ingrese un numero que nuestro sistema pueda procesar! ❌\n\n")
        except ValueError:
            print("❌ Ingrese un numero que nuestro sistema pueda procesar! ❌\n\n")
        
    print("➖" * 70)
    largo = -1
    ancho = -1
    espesor = -1
    while largo < 0:
        try:
            largo = float(input("📏 Ingrese largo del espacio que desea cubrir (SOLO EL NUMERO): "))
            if largo < 0:
                print("❌ Ingrese un numero que nuestro sistema pueda procesar! ❌\n\n")
        except ValueError: 
            print("❌ Ingrese un numero que nuestro sistema pueda procesar! ❌\n")
    while ancho < 0:
        try:
            ancho = float(input("📏 Ingrese ancho del espacio que desea cubrir (SOLO EL NUMERO): "))
            if ancho < 0:
                print("❌ Ingrese un numero que nuestro sistema pueda procesar! ❌\n\n")
        except ValueError:
            print("❌ Ingrese un numero que nuestro sistema pueda procesar! ❌\n")
    
    while espesor < 0:
        try:
            espesor = float(input("📏 Ingrese altura del espacio que desea cubrir (SOLO EL NUMERO): "))
            if espesor < 0:
                print("❌ Ingrese un numero que nuestro sistema pueda procesar! ❌\n\n")
        except ValueError:
            print("❌ Ingrese un numero que nuestro sistema pueda procesar! ❌\n")
    if unidad == 2 : # Convierte cm a mts.
        ancho /= 100 
        largo /= 100
        espesor /= 100
    elif unidad == 3 : # Convierte pies a mts.
        ancho *= 0.3048
        largo *= 0.3048
        espesor *= 0.3048

    volumen = ancho * largo * espesor

    # CALCULO PROPORCIONES DE CEMENTO, ARENA Y GRAVA

    cantidad_cemento = (volumen * 350)* 1.05 # el 1.05 es porq le sumamos un desperdicio del 5%
    bolsas_cemento = cantidad_cemento // 50 # suponiendo que las bolsas de cemento son de 50kg

    if cantidad_cemento%50 != 0:
        bolsas_cemento = bolsas_cemento + 1 # aca hago q si necesita una cantidad de bolsas con decimal, le añade una extra

    cantidad_arena = volumen * 0.56 # esto nos va a arrojar la cantidad de metros cubicos de arena necesarios
    kg_de_arena = cantidad_arena * 1529.20 # con esto logramos pasar los metros cubicos a kg de arena
    bolsas_arena = kg_de_arena // 25 # suponiendo q las bolsas de arena son de 25kg (en mercado libre las q venden son de eso)
    if cantidad_arena%25 != 0:
        bolsas_arena = bolsas_arena + 1 # aca hago que si me da un numero con coma me agregue una

    cantidad_grava = volumen * 0.84 # esto nos va a arrojoar la cantidad de metros cubicos de grava necesaria
    kg_de_grava = cantidad_grava * 1.680 # con esto logramos pasar los metros cubicos a kg de grava
    bolsas_grava = kg_de_grava // 20  # suponiendo que la bolsa de grava es de 20kg (en mercado libre las q venden son de eso)
    if kg_de_grava%20 !=0:
        bolsas_grava= bolsas_grava + 1 # aca hago que si le da 21,3 bolsas por ejemplo le muestre 22

    agua_necesaria = volumen * 180 # esto nos dice la cantidad de agua maxima a utiliza, no lo vendemos solo se lo recordamos al cliente

    print("➖" * 70)
    print("🧍Estimado/a ", cliente.upper())

    print("El volumen a cubrir segun las medidas anteriormente mencionadas es de: ", volumen, "m³")
    print("Por lo que se requeriran ", int(bolsas_cemento), " bolsa de cemento (x50kg)")
    print("Por lo que se requeriran ", int(bolsas_arena), " bolsas de arena (x25kg) ")
    print("Por lo que se requeriran ", int(bolsas_grava), " bolsa de grava (x20kg) ")
    print("⚠️  RECUERDE NO EXCEDERSE DE LOS MAXIMOS", int(agua_necesaria), " LITROS DE AGUA YA QUE EL CEMENTO PERDERA RESISTENCIA ")
    print("☎️   353-154928734")
    print("📩  Corraloneltiokevin@gmail.com")
    print("📍  Av. Universidad 450, X5900 Villa María, Córdoba")
    print("➖" * 70)

    desea_continuar = float(input(f"¿Desea continuar ?\n\t\t1 - Si.\n\t\t2 - No.\n\n\n> > > "))

    # TICKET PARA EL CLIENTE.
    archivo_control = f"{cliente}_{apellido}_recibo.txt"
    f = open(archivo_control,"w")
    f.write(f"-------------------------------------------------------\n"
            f"CLIENTE : {apellido}, {cliente}\n"
            f"DNI : {dni}\n"
            f"-------------------------------------------------------\n"
            f"\t - un total de {volumen} m³ a cubrir. \n"
            f"\t - {bolsas_cemento} bolsa/s de cemento (x50kg).\n"
            f"\t - {bolsas_arena} bolsa/s de arena (x25kg).\n"
            f"\t - {bolsas_grava} bolsa/s de grava (x20kg). \n"
            f"-------------------------------------------------------\n"
            f"CORRALON EL TIO KEVIN \n"
            f"TEL : 353-154928734 \n"
            f"corraloneltiokevin@gmail.com \n"
            f"Av. Universidad 450, X5900 Villa María, Córdoba"
            )
    f.close()

    # HISTORIAL DE CLIENTES PARA LA EMPRESA.

    agenda = "agenda.txt"
    g = open(agenda, "a")
    g.write(f"-------------------------------------------------------\n"
            f"DNI : {dni}\n"
            f"CLIENTE : {apellido} {cliente}\n"
            f"TEL : {telefono}\n"
            f"-------------------------------------------------------\n")
    g.close()

    # HISTORIAL DE VENTAS

    libro_ventas = "ventas.txt"
    h = open(libro_ventas, "a")
    h.write(f"-------------------------------------------------------\n"
            f"CLIENTE : {apellido}, {cliente}\n"
            f"DNI : {dni}\n"
            f"TELEFONO : {telefono}\n"
            f"\t - un total de {volumen} m³ a cubrir. \n"
            f"\t - {bolsas_cemento} bolsa/s de cemento (x50kg).\n"
            f"\t - {bolsas_arena} bolsa/s de arena (x25kg).\n"
            f"\t - {bolsas_grava} bolsa/s de grava (x20kg). \n"
            )
    h.close()

    os.system("cls")

    if desea_continuar == 2:
        break