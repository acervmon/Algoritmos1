if __name__ == "__main__":
    from Interfaz import Interfaz
    from Polinomio import polinomio1, polinomio2
    from nodo import nodo
    from Realizador import sumar, multiplicar, restar, dividir, mostrar

    print("Polinomio 1:", mostrar(polinomio1))
    print("Polinomio 2:", mostrar(polinomio2))
    print("Suma:", mostrar(sumar(polinomio1, polinomio2)))
    print("Resta:", mostrar(restar(polinomio1, polinomio2)))
    print("Multiplicación:", mostrar(multiplicar(polinomio1, polinomio2)))
    print("División:", mostrar(dividir(polinomio1, polinomio2)))
