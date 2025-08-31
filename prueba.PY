import random
#Lista de valores posibles para las filas
Simbolos = ["7️⃣", "🍋",  "🍒" ]

input("Bienvenido a la maquina tragaperras presione enter para apostar       ")
while True:
    #definir cada una de las filas, con un valor ramdom de Simbolos
    c1f1 = "7️⃣"
    c1f2 = "7️⃣"
    c1f3 = "7️⃣"
    c2f1 = "7️⃣"
    c2f2 = "7️⃣"
    c2f3 = "7️⃣"
    c3f1 = "7️⃣"
    c3f2 = "7️⃣"
    c3f3 = "7️⃣"
    #Preguntarle al Usuario en cuantas lineas desea apostar
    Num_lineas = int(input("En cuantas lineas desea apostar? "))
    #Si el usuario ingresa un numero no valido volverlo a pedir
    while Num_lineas not in [1, 2, 3]:
        Num_lineas = int(input("Por favor ingrese un número de líneas válido (1-3): "))
       

    print("lINEA 1     ",c1f1,"    ", c1f2,"    ",  c1f3)
    print("lINEA 2     ",c2f1,"    ", c2f2,"    ",  c2f3)
    print("lINEA 3     ",c3f1,"    ", c3f2,"    ",  c3f3)

    #RESULTADOS 
    
    
    if Num_lineas == 1: #Si el numero de lineas elejido es igual a 1
        if c2f1 == c2f2 == c2f3 or c1f1 == c1f2 == c1f3 or c3f1 == c3f2 == c3f3:
            print ("felicidades has ganado") 
        else:
            print("has perdido")
    elif Num_lineas == 2: #Si el numero de lineas elejido es igual a 2
        #Si l2 = l1                                         Si l2=l3                                         Si L1 = L3 
        if c2f1 == c2f2 == c2f3 and c1f1 == c1f2 == c1f3 or c2f1 == c2f2 == c2f3 and c3f1 == c3f2 == c3f3 or c1f1 == c1f2 == c1f3 and c3f1 == c3f2 == c3f3:
            print ("felicidades has ganado en dos lineas") 
        elif c2f1 == c2f2 == c2f3 or c1f1 == c1f2 == c1f3 or c3f1 == c3f2 == c3f3:
            print ("ganaste solo en una linea")
        else:
            print("has perdido")
    else:#Si el numero de lineas elejido es igual a 3

        if c1f1 == c1f2 == c1f3 and c2f1 == c2f2 == c2f3 and c3f1 == c3f2 == c3f3:
            print("¡Felicidades has ganado en las tres líneas!")

        elif c2f1 == c2f2 == c2f3 and c1f1 == c1f2 == c1f3 or c2f1 == c2f2 == c2f3 and c3f1 == c3f2 == c3f3 or c1f1 == c1f2 == c1f3 and c3f1 == c3f2 == c3f3:
            print ("felicidades has ganado en dos lineas") 
        elif c2f1 == c2f2 == c2f3 or c1f1 == c1f2 == c1f3 or c3f1 == c3f2 == c3f3:
            print ("ganaste solo en una linea")
        else:
            print("has perdido")
        
    # Opciones para seguir jugando o dejar de jugar
    Seguir_apostando = input ("Escriba \"Si\" si desea seguir apostando, si no escriba \"No\" "      ).strip().lower()
    if Seguir_apostando != "si":
        print ("Gracias por jugar")
        break