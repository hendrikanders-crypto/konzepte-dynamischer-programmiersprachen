import math
a = float(input("Radius r: "))
b = float(input("Höhe h: "))

Volumen = math.pi * a**2 * b
Oberflaeche = 2 * math.pi * a ** 2 + 2 * math.pi * a * b

print("Volumen des Zylinders:", Volumen)
print("Oberfläche des Zylinders:", Oberflaeche)