
#encoding:UTF-8
import random

aleatorio = random.randrange(0, 3)
eligePc = ""
print("1)Piedra")
print("2)Papel")
print("3)Tijera")
opcion = int(input("Que eliges: "))

if opcion == 1:
    eligeUsuario = "piedra"
elif opcion == 2:
    eligeUsuario = "papel"
elif opcion == 3:
    elijeUsuario = "tijera"
print("Tu eliges: ", eligeUsuario)

if aleatorio == 0:
    eligePc = "piedra"
elif aleatorio == 1:
    eligePc = "papel"
elif aleatorio == 2:
    eligePc = "tijera"
print("PC eligió: ", eligePc)
print("...")
if eligePc == "piedra" and eligeUsuario == "papel":
    print("Ganaste, papel envuelve piedra")
elif eligePc == "papel" and eligeUsuario == "tijera":
    print("Ganaste, Tijera corta papel")
elif eligePc == "tijera" and eligeUsuario == "piedra":
    print("Ganaste, Piedra pisa tijera")
if eligePc == "papel" and eligeUsuario == "piedra":
    print("perdiste, papel envuelve piedra")
elif eligePc == "tijera" and eligeUsuario == "papel":
    print("perdiste, Tijera corta papel")
elif eligePc == "piedra" and eligeUsuario == "tijera":
    print("perdiste, Piedra pisa tijera")
elif eligePc == eligeUsuario:
    print("empate")
