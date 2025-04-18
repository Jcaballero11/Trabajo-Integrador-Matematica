print("Conversor de números - UTN TUPaD - Comisión 10")

#while true permite volver a entrar en el input
#mientras sea verdadera la condición, se ejecuta el bloque de código
#esta para validar que el usuario no ingrese otro numero que no sea 1, 2 o 3

while True: #lo usamos para poder repetir que el usuario ingrese un número. 
            #El while True lo que hace es que es un bucle infinito mientras lo que ingrese no sea válido.
            #Si el número es válido, el codigo sigue y el break hace que el bucle se detenga y el programa continúe.
            #Este bucle infinito se utiliza para mostrar el menú una y otra vez hasta que el usuario elija salir o dé una opción válida.
            #La única forma de salir de un while True es con un break.
    print("Elija una opción (1, 2 o 3):") #Acá se muestran las opciones del menú para que el usuario elija qué conversión desea hacer.
    print("1. Pasar de decimal a binario")
    print("2. Pasar de binario a decimal")
    print("3. Salir del programa")

    eleccion = input() #Se espera a que el usuario ingrese su elección. Lo que escriba se guarda en la variable eleccion.

    if eleccion == '1': #Si el usuario eligió la opción 1, entra a otro while True (otro bucle infinito),
                        #ahora para validar que el número ingresado sea un decimal positivo válido.
        while True: #lo usamos para poder repetir que el usuario ingrese un número
            numero_decimal = input("Ingresá un número decimal positivo: ") #Se le pide al usuario que ingrese un número decimal.

            if numero_decimal != "": #Se verifica que no haya dejado el campo vacío.
                for num in numero_decimal: #recorre el numero ingresado uno por uno para buscar si hay algun error
                    if num not in '0123456789': #Se recorre cada carácter ingresado para asegurarse de que todos sean dígitos del 0 al 9.
                                                #Si encuentra una letra o símbolo, avisa que es inválido y vuelve a pedir el número.
                        print("Número decimal inválido! Coloque números del 0 al 9.")
                        break
                else: #Si pasa todas las validaciones:
                    decimal = int(numero_decimal) #Se convierte el texto a número entero (int)
                    binario = bin(decimal)[2:] #bin() convierte numero decimal a binario pero con un "0b" al principio, se hace un "slicing" con [2:] (borra los dos primeros caracteres del string)
                    print("El número", decimal, "en binario es:", binario) #Finalmente, se muestra el número convertido y se hace un break para salir del bucle
                    print()  #línea en blanco para separar
                    break
    ############################################################################################################################################################

    elif eleccion == '2':
        while True: #lo usamos para poder repetir que el usuario ingrese un número
            numero_binario = input("Ingresá un número binario (0 y 1): ")

            if numero_binario != "": #esto es para evitar que no quede vacío el input
                for num in numero_binario: #recorre el numero ingresado uno por uno para buscar si hay algun error
                    if num != '0' and num != '1':
                        print("Número binario inválido! Coloque solo 0 y 1.")
                        break
                else:
                    decimal = int(numero_binario, 2) #covertimos el texto a número, y el "2" lo utilizamos para pasar de decimal a binario ya que es en base 2
                    print("El número binario", numero_binario, "en decimal es:", decimal)
                    print()  #línea en blanco para separar
                    break

    elif eleccion == '3':
        print("Saludos!")
        break

    else:
        print("Opción no válida! Elegí 1, 2 o 3.")
        print()  #línea en blanco para separar

#bin(decimal) pasa el número decimal a binario, pero con un "0b" al principio
#0b10101 con "slicing" con [2:] (borra los dos primeros caracteres del string)
