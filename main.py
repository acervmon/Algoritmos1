import polinomio
from polinomio import Polinomio
def menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    print("Defina el Polinomio 1")
    polinomio1 = Polinomio()

    print("Defina el Polinomio 2")
    polinomio2 = Polinomio()

    print("Polinomio 1:")
    polinomio1.mostrar()

    print("Polinomio 2:")
    polinomio2.mostrar()

    while True:
        menu()
        opcion = int(input("Opción: "))

        if opcion == 1:
            resultado = Polinomio.sumar(polinomio1, polinomio2)
            print("Resultado:")
            resultado.mostrar()
        elif opcion == 2:
            resultado = Polinomio.restar(polinomio1, polinomio2)
            print("Resultado:")
            resultado.mostrar()
        elif opcion == 3:
            resultado = Polinomio.multiplicar(polinomio1, polinomio2)
            print("Resultado:")
            resultado.mostrar()
        elif opcion == 4:
            resultado = Polinomio.dividir(polinomio1, polinomio2)
            print("Resultado:")
            resultado.mostrar()
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
