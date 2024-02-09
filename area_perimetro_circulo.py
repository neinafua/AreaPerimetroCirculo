import math

# imput
print("-----------------------------")
r = input("ingrese el valor del radio del circulo:  ")
r = int(r)

# processing
a = math.pi*r*r
p = 2*math.pi*r

#output
print("-----------------------------")
print("El área es: " + str(a))
print("El perímetro es: " + str(p))
print("-----------------------------")