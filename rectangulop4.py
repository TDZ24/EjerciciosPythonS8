# Rectangulo

ancho = int(input("Ingrese el ancho del rectangulo: "))
altura = int(input("Ingrese el altura del rectangulo: "))


base = ancho*altura
print(f"La base del rectangulo es {base}")

perimetro = 2*(base)+2*(altura)
print(f"El perimetro del rectangulo es {perimetro}")

for i in range(1, altura+1):
    for j in range(1, ancho+1):
        print("*", end="")
    print(" ")
