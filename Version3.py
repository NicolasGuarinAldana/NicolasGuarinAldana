import random
#Lista de valores posibles para las filas
Simbolos = ["7️⃣", "🍋",  "🍒" ]

input("Bienvenido a la maquina tragaperras presione enter para apostar       ")
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
       

    print("lINEA 1     ",c1f1,"    ", c1f2,"    ",  c1f3)
    print("lINEA 2     ",c2f1,"    ", c2f2,"    ",  c2f3)
    print("lINEA 3     ",c3f1,"    ", c3f2,"    ",  c3f3)

        
    
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
            print ("felicidades has ganado") 
        else:
            print("has perdido")

    #Si el numero de lineas elejido es igual a 2
    elif Num_lineas == 2: 
        
        if Linea1 == 1 and Linea2 == 1 or Linea1 == 1 and Linea3 == 1 or Linea2 == 1 and Linea3 == 1:
            print ("felicidades has ganado en dos lineas") 
        elif Linea1 == "Verdadero" or Linea2 == "Verdadero" or Linea3 == "Verdadero":
            print ("ganaste solo en una linea")
        else:
            print("has perdido")

    #Si el numero de lineas elejido es igual a 3
    else:

        if Linea1 == 1 and Linea2 == 1 and Linea3 == 1:
            print ("felicidades has ganado en las 3 lineas")
        elif  Linea1 == 1 and Linea2 == 1 or Linea1 == 1 and Linea3 == 1 or Linea2 == 1 and Linea3 == 1:
            print ("felicidades has ganado en dos lineas") 
        elif Linea1 == 1 or Linea2 == 1 or Linea3 == 1:
            print ("ganaste solo en una linea")
        else:
            print("has perdido")
        
    # Opciones para seguir jugando o dejar de jugar
    Seguir_apostando = input ("Escriba \"Si\" si desea seguir apostando, si no escriba \"No\" "      ).strip().lower()
    if Seguir_apostando != "si":
        print ("Gracias por jugar")
        break