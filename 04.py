'''for i in range(3,-13,-3):
    print(f"El valor del bucle es: {i}.")
print("fin del bucle")'''

colores = ["rojo", "azul", "verde", "amarillo"]

print("listado de colores")

'''for color in colores:
    if color == "azul" or color == "verde":
        print("Se ha saltado este valor")
        continue
    print(f"-color {color}")'''

'''for color in colores:
    if color == "azul":
        print("Se ha roto el bucle")
        break
    print(f"-color {color}")'''
    
'''i = 1

while i <= 5:
    print(f"el valor del bucle es: {i}")
    i += 1'''
    
'''i = 1

while i >= -5:
    print(f"el valor del bucle es: {i}")
    i -= 1'''
    
while True:
    salida = input("introduce 'salir' para finalizar\n"). lower()
    if salida == 'salir':
        break