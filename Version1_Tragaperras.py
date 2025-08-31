import random
#Lista de valores posibles para las filas
Simbolos = ["7️⃣", "🍋",  "🍒" ]

input("Bienvenido a la maquina tragaperras presione enter para apostar       ")
while True:
    #definir cada una de las filas, con un valor ramdom de Simbolos
    fila_1 = random.choice(Simbolos)
    fila_2 = random.choice(Simbolos)
    fila_3 = random.choice(Simbolos)

    print (fila_1,"       " , fila_2,"        ", fila_3)
    if fila_1 == fila_2 == fila_3: # Funcion que define si el usuario gano o perdio
        print("felicidades has ganado")
    else:
        print("has perdido")
    # Opciones para seguir jugando o dejar de jugar
    Seguir_apostando = input ("Escriba \"Si\" si desea seguir apostando, si no escriba \"No\" "      ).strip().lower()
    if Seguir_apostando != "si":
        print ("Gracias por jugar")
        break
