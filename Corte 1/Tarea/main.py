from clase import Operaciones # type: ignore
    
def main():
    calc = Operaciones()

    print("¡¡Holaaa!!")
    print("Bienvenido a la calculadora básica, espero te sea muy útil...")
    print("Primero selecciona la operación que deseas realizar, para esto escribe el número correspondiente como se indica:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input("Escribe aquí el número de la operación que deseas realizar: "))
    num1 = float(input("Ahora escribe el primer número de tu operación: "))
    num2 = float(input("Y por último, escribe el segundo número: "))

    if opcion == 1:
        print("Resultado de tu operación es:", calc.suma(num1, num2))
    elif opcion == 2:
        print("Resultado de tu operación es:", calc.resta(num1, num2))
    elif opcion == 3:
        print("Resultado de tu operación es:", calc.multiplicacion(num1, num2))
    elif opcion == 4:
        print("Resultado de tu operación es:", calc.division(num1, num2))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

    