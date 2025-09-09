import random
#Lista de valores posibles para las filas
Simbolos = ["💎", "🍋",  "🍒" ]

print ("🎰     Bienvenido a la maquina tragaperras     🎰 ")

print("╔════════════════════════════════════════════════╗")
print("║                🎰 TRAGAPERRAS 🎰               ║")
print("╠════════════════════════════════════════════════╣")
print("║ LINEA 1  →           💎  |  🍋  |  🍒          ║")
print("║ LINEA 2  →           💎  |  🍒  |  🍋          ║")
print("║ LINEA 3  →           💎  |  🍋  |  🍒          ║")
print("╚════════════════════════════════════════════════╝")


# Definir un saldo correcto
while True:
    try:
        Saldo = int(input("Cuánto dinero desea Apostar (la apuesta minima es 100): "))

        if Saldo < 100:  
            print("❌ El saldo debe ser un número positivo mayor que 100.")
            continue

        break  

    except ValueError:
        print("❌ Por favor escriba un valor correcto (solo números).")



while True:
    #definir cada una de las filas, con un valor ramdom de Simbolos
    c1f1 = random.choice(Simbolos)
    c1f2 = random.choice(Simbolos)
    c1f3 =random.choice(Simbolos)
    c2f1 = random.choice(Simbolos)
    c2f2 = random.choice(Simbolos)
    c2f3 =random.choice(Simbolos)
    c3f1 = random.choice(Simbolos)
    c3f2 = random.choice(Simbolos)
    c3f3 =random.choice(Simbolos)
    
    #Preguntarle al Usuario en cuantas lineas desea apostar
    Num_lineas = int(input("En cuantas lineas desea apostar? "))
    
    #Si el usuario ingresa un numero no valido volverlo a pedir
    
    while Num_lineas not in [1, 2, 3]:
        Num_lineas = int(input("Por favor ingrese un número de líneas válido (1-3): "))


    while True:
        try:
            Apuesta_por_Linea = int(input(f"¿Cuánto dinero desea apostar por línea? Tu saldo es: {Saldo} → "))

            # Validación 0: no puede ser 0 o negativo
            if Apuesta_por_Linea <= 0:
                print("❌ La apuesta debe ser un número positivo mayor que 0.")
                continue  

            # Validación 1: no puede ser mayor al saldo total
            if Apuesta_por_Linea > Saldo:
                print("❌ No tiene el suficiente saldo para realizar esta apuesta.")
                continue  

            # Validación 2: depende del número de líneas
            if Apuesta_por_Linea > Saldo / Num_lineas:
                print(f"❌ Saldo insuficiente para {Num_lineas} líneas. Intente con una apuesta menor.")
                continue  

            # ✅ Si pasa todas las validaciones, se acepta la apuesta
            break  

        except ValueError:
            print("❌ Por favor escriba un número válido.")



    Saldo -= Apuesta_por_Linea


        


    #MOSTRAR LA MAQUINA EN FUNCIONAMIENTO
    print("╔════════════════════════════════════════════════╗")
    print("║                🎰 TRAGAPERRAS 🎰               ║")
    print("╠════════════════════════════════════════════════╣")
    print(f"║ LINEA 1  →           {c1f1}  |  {c1f2}  |  {c1f3}          ║")
    print(f"║ LINEA 2  →           {c2f1}  |  {c2f2}  |  {c2f3}          ║")
    print(f"║ LINEA 3  →           {c3f1}  |  {c3f2}  |  {c3f3}          ║")
    print("╚════════════════════════════════════════════════╝")

        
    
    #Resultados Linea1 
    if c1f1 == c1f2 == c1f3:
        Linea1 = 1       # 1 Significa que gano en esa linea
    else:
        Linea1 = 0       #0 siginifica que perdio en esa li

    #Resultados Linea2
    if  c2f1 == c2f2 == c3f2:
        Linea2 = 1
    else:
        Linea2 = 0
    
    #Resultados Linea3
    if c3f1 == c3f2 == c3f3:
        Linea3 = 1
    else:
        Linea3 = 0    
    
    #Si el numero de lineas elejido es igual a 1    
    if Num_lineas == 1: 
        if Linea1 == 1 or Linea2 == 1 or Linea3 == 1:
            Apuesta_por_Linea *= 2
            print (f"felicidades has ganado {Apuesta_por_Linea}")     
            Saldo +=  Apuesta_por_Linea
        else:
            print("has perdido")

    #Si el numero de lineas elejido es igual a 2
    elif Num_lineas == 2: 
        
        if Linea1 == 1 and Linea2 == 1 or Linea1 == 1 and Linea3 == 1 or Linea2 == 1 and Linea3 == 1:
            Apuesta_por_Linea *=4
            Saldo += Apuesta_por_Linea
            print (f"felicidades has ganado en dos lineas, ganaste {Apuesta_por_Linea} ")  
            
              
        elif Linea1 == "Verdadero" or Linea2 == "Verdadero" or Linea3 == "Verdadero":
            Apuesta_por_Linea *= 2
            print (f"ganaste solo en una linea, ganaste {Apuesta_por_Linea}")
            Saldo += Apuesta_por_Linea 

        else:
            print("has perdido")

    #Si el numero de lineas elejido es igual a 3
    else:

        if Linea1 == 1 and Linea2 == 1 and Linea3 == 1:
            Apuesta_por_Linea *=6
            Saldo += Apuesta_por_Linea
            print (f"felicidades has ganado en las 3 lineas, ganaste {Apuesta_por_Linea}")
        elif  Linea1 == 1 and Linea2 == 1 or Linea1 == 1 and Linea3 == 1 or Linea2 == 1 and Linea3 == 1:
            Apuesta_por_Linea *=4
            Saldo += Apuesta_por_Linea
            print (f"felicidades has ganado en dos lineas, ganaste {Apuesta_por_Linea} ")  
        elif Linea1 == 1 or Linea2 == 1 or Linea3 == 1:
            Apuesta_por_Linea *= 2
            print (f"ganaste solo en una linea, ganaste {Apuesta_por_Linea}")
            Saldo += Apuesta_por_Linea 


        else:
            print("has perdido")
        
    # Opciones para seguir jugando o dejar de jugar
    print (f"Tu saldo es igual a {Saldo}")
    Seguir_apostando = input ("Escriba \"Si\" si desea seguir apostando, si no escriba \"No\" "      ).strip().lower()
    if Seguir_apostando != "si":
        print ("Gracias por jugar")
        break  