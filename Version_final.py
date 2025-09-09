import random
import sys
#Lista de valores posibles para las filas
Simbolos = ["💎", "🍋",  "🍒" ]

print ("✨🎰     Bienvenido a la máquina tragaperras     🎰✨")

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
        Saldo = int(input("💰 ¿Cuánto dinero desea Apostar? (mínimo 100): "))

        if Saldo < 100:  
            print("❌ El saldo debe ser mayor o igual a 100.")
            continue

        break  

    except ValueError:
        print("❌ Por favor escriba un valor correcto (solo números).")



while True:
    #definir cada una de las filas, con un valor random de Simbolos
    c1f1 = random.choice(Simbolos)
    c1f2 = random.choice(Simbolos)
    c1f3 = random.choice(Simbolos)
    c2f1 = random.choice(Simbolos)
    c2f2 = random.choice(Simbolos)
    c2f3 = random.choice(Simbolos)
    c3f1 = random.choice(Simbolos)
    c3f2 = random.choice(Simbolos)
    c3f3 = random.choice(Simbolos)
    
    #Preguntarle al Usuario en cuantas lineas desea apostar
    Num_lineas = int(input("➡️  ¿En cuántas líneas desea apostar? (1-3): "))
    
    #Si el usuario ingresa un numero no valido volverlo a pedir
    while Num_lineas not in [1, 2, 3]:
        Num_lineas = int(input("❌ Número inválido. Ingrese un valor entre 1 y 3: "))


    while True:
        try:
            Apuesta_por_Linea = int(input(f"🎯 ¿Cuánto dinero desea apostar por línea? Tu saldo es: 💳 {Saldo} → "))

            # Validación 0: no puede ser 0 o negativo
            if Apuesta_por_Linea <= 0:
                print("❌ La apuesta debe ser mayor que 0.")
                continue  

            # Validación 1: no puede ser mayor al saldo total
            if Apuesta_por_Linea > Saldo:
                print("❌ No tiene el suficiente saldo para realizar esta apuesta.")
                continue  

            # Validación 2: depende del número de líneas
            if Apuesta_por_Linea > Saldo / Num_lineas:
                print(f"⚠️ Saldo insuficiente para {Num_lineas} líneas. Intente con una apuesta menor.")
                continue  

            # ✅ Si pasa todas las validaciones, se acepta la apuesta
            break  

        except ValueError:
            print("❌ Por favor escriba un número válido.")

    Saldo -= Apuesta_por_Linea

    #MOSTRAR LA MAQUINA EN FUNCIONAMIENTO
    print("\n🎰 GIRANDO LOS RODILLOS... 🎰\n")
    print("╔════════════════════════════════════════════════╗")
    print("║                ✨ TRAGAPERRAS ✨               ║")
    print("╠════════════════════════════════════════════════╣")
    print(f"║ LINEA 1  →           {c1f1}  |  {c1f2}  |  {c1f3}          ║")
    print(f"║ LINEA 2  →           {c2f1}  |  {c2f2}  |  {c2f3}          ║")
    print(f"║ LINEA 3  →           {c3f1}  |  {c3f2}  |  {c3f3}          ║")
    print("╚════════════════════════════════════════════════╝")

    #Resultados Linea1 
    if c1f1 == c1f2 == c1f3:
        Linea1 = 1
    else:
        Linea1 = 0

    #Resultados Linea2
    if  c2f1 == c2f2 == c2f3:
        Linea2 = 1
    else:
        Linea2 = 0
    
    #Resultados Linea3
    if c3f1 == c3f2 == c3f3:
        Linea3 = 1
    else:
        Linea3 = 0    
    
    #Si el numero de lineas elegido es igual a 1    
    if Num_lineas == 1: 
        if Linea1 + Linea2 + Linea3 == 1:
            Apuesta_por_Linea *= 4
            print (f"🎉 Felicidades, ganaste {Apuesta_por_Linea} 💰")     
            Saldo +=  Apuesta_por_Linea
        else:
            print("💀 Has perdido esta vez...")

    #Si el numero de lineas elegido es igual a 2
    elif Num_lineas == 2: 
        if Linea1 + Linea2 + Linea3 == 2:
            Apuesta_por_Linea *=8
            Saldo += Apuesta_por_Linea
            print (f"🎉 ¡Ganaste en dos líneas! Premio: {Apuesta_por_Linea} 💰")  
        elif Linea1 + Linea2 + Linea3 == 1:
            Apuesta_por_Linea *= 4
            print (f"😎 Ganaste en una sola línea, premio: {Apuesta_por_Linea} 💰")
            Saldo += Apuesta_por_Linea 
        else:
            print("💀 Has perdido esta vez...")

    #Si el numero de lineas elegido es igual a 3
    else:
        if Linea1 + Linea2 + Linea3 == 3:
            Apuesta_por_Linea *=12
            Saldo += Apuesta_por_Linea
            print (f"🏆 ¡Jackpot! Ganaste en las 3 líneas: {Apuesta_por_Linea} 💰")
        elif Linea1 + Linea2 + Linea3 == 2:
            Apuesta_por_Linea *=4
            Saldo += Apuesta_por_Linea
            print (f"🎉 ¡Muy bien! Ganaste en dos líneas: {Apuesta_por_Linea} 💰")  
        elif Linea1 + Linea2 + Linea3 == 1:
            Apuesta_por_Linea *= 2
            print (f"😎 Ganaste en una línea: {Apuesta_por_Linea} 💰")
            Saldo += Apuesta_por_Linea 
        else:
            print("💀 Has perdido esta vez...")

    # Opciones para seguir jugando o dejar de jugar
    while True:
        print(f"\n💳 Tu saldo actual es: {Saldo}")
        print("👉 Presiona Enter para seguir jugando")
        print("👉 Escribe 'q' para retirar dinero y salir")
        print("👉 Escribe 'm' para introducir más saldo")

        opcion = input("➡️ Elige una opción: ").strip().lower()

        if opcion == "q":  # retirar y salir 
        
            print(f"🏦 Retiraste {Saldo} 💰. ¡Gracias por jugar! 🎰")
            sys.exit()
        

        elif opcion == "m":  # meter más saldo
            try:
                extra = int(input("💵 ¿Cuánto dinero deseas agregar?: "))
                if extra > 0:
                    Saldo += extra
                    print(f"✅ Se agregaron {extra} al saldo. Nuevo saldo: {Saldo}")
                else:
                    print("❌ Debes ingresar un número positivo.")
            except ValueError:
                print("❌ Por favor escribe un número válido.")
    
        else:  # Enter u otra tecla para seguir jugando 
            print("🎰 ¡A girar de nuevo!")
            #  vuelve al bucle principal
            continue

