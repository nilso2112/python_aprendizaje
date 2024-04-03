# Se le pide la edad al usuario.
'''
edad = int(input("Introduzca su edad:\n"))

# Se deja la variable sin valor.
respuesta = None

# Se evalúa si el usuario es mayor de edad. Si lo es, accede a
# la compra de alcohol.
if edad >= 18:
    print("Es mayor de edad, puede comprar alcohol. ¿Cuál desea? Introduzca un número de opción.")
    respuesta = input("1- ron.\n2- whisky.\n3- ginebra.\n")

    if respuesta == "1":
        print("Ha elegido comprar ron.")
    elif respuesta == "2":
        print("Ha elegido comprar whisky.")
    elif respuesta == "3":
        print("Ha elegido comprar ginebra.")
    else:
        print("Opción no válida.")
else:
    print("Es menor de edad, vuelva de aquí un tiempo o no empiece con el alcohol.")
'''
'''
color = "rojo"
forma = "circulo"
tamano = "grande"

if color == "rojo" and forma == "circulo":
    print("Es un circulo rojo")
else:
    print ("No se cumple la condicion")'''
    
'''if color == "rojo" or forma == "circulo" or tamano == "grande":
    print("se cumple la condicion")
else:
    print ("No se cumple la condicion")'''
    
'''if not(color == "azul" and forma == "cuadrado"):
    print("se cumple la condicion")
else:
    print ("No se cumple la condicion")
    
if not(color == "azul" and forma == "cuadrado"):
    print("se cumple la condicion")
else:
    print ("No se cumple la condicion")'''
    
'''
error = input('Introduzca un código de error:\n')
 
match error:
    case "200":
        print('Todo ok.')
    case "301":
        print('Movimiento permanente de la página.')
    case "302":
        print('Movimiento temporal de la página.')
    case "404":
        print('Página no encontrada.')
    case "500":
        print('Error interno del servidor.')
    case "503":
        print('Servicio no disponible.')
    case defecto:
        print('Error no disponible.')
'''

'''Un título para la calculadora.
El usuario podrá decidir que operación desea antes de introducir los operandos (números con los que operar). Con el fin de informar al usuario de cada opción, crea un menú con varios print(). Por ejemplo, print("1-Suma").
Se debe avisar al usuario de la opción que ha seleccionado.
Si el usuario elige una opción que no está en el menú, se le debe avisar del error.
Entrada de datos para dos números float.
Hay que crear un sistema que realice las operaciones.
Se le deberá mostrar el resultado correctamente al usuario.
Opcionalmente, le puedes añadir un redondeo (round()) a las operaciones, para que el resultado solo muestre dos dígitos.
Otro requisito opcional más complicado, es añadir, de alguna forma, un control para el caso en el que el usuario ponga una opción inválida (no se contemplarán los errores de tipo de dato todavía).
'''

print("--CALCULADORA--")

print("Seleccione una opcion")
print("1.- suma")
print("2.- resta")
print("3.- multiplicacion")
print("4.- division")
print("5.- modulo")
print("6.- Exponente")

opcion = int(input("Teclee un numero y pulse ENTER:\n"))
error = True

match opcion:
    case 1:
        print('Ha elegido la opción "suma".')
    case 2:
        print('Ha elegido la opción "resta".')
    case 3:
        print('Ha elegido la opción "multiplicación".')
    case 4:
        print('Ha elegido la opción "división".')
    case 5:
        print('Ha elegido la opción "módulo".')
    case 6:
        print('Ha elegido la opción "exponente".')
    case _:
        print('Error, opción inválida.')
        error = False
        
if error == True:
    numero_1 = float(input("Especifique el primer operando:\n"))
    numero_2 = float(input("Especifique el segundo operando:\n"))
    
    match opcion:
        case 1:
            resultado = round(numero_1 + numero_2, 2)
            print(f"El resultado de sumar {numero_1} + {numero_2} es: {resultado}.")
        case 2:
            resultado = round(numero_1 - numero_2, 2)
            print(f"El resultado de restar {numero_1} - {numero_2} es: {resultado}.")
        case 3:
            resultado = round(numero_1 * numero_2, 2)
            print(f"El resultado de multiplicar {numero_1} por {numero_2} es: {resultado}.")
        case 4:
            resultado = round(numero_1 / numero_2, 2)
            print(f"El resultado de dividir {numero_1} entre {numero_2} es: {resultado}.")
        case 5:
            resultado = round(numero_1 % numero_2, 2)
            print(f"El resto de la división de {numero_1} entre {numero_2} es: {resultado}.")
        case 6:
            resultado = round(numero_1 ** numero_2, 2)
            print(f"{numero_1} elevado a {numero_2} es: {resultado}.")
else:
    print("Por favor, vuelva a ejecutar la calculadora.")


