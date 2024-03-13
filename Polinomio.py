class Polinomio:
    def __init__(self):
        self.grado = int(input("Ingrese el grado del polinomio: "))
        self.polinomio = []
        self.llenar_polinomio()

    def llenar_polinomio(self):
        for i in range(self.grado + 1):
            while True:
                try:
                    coeficiente = float(input(f"Ingrese el coeficiente para x^{i}: "))
                    break
                except ValueError:
                    print("Error: Ingrese un número válido.")
            self.polinomio.append(coeficiente)

polinomio1 = Polinomio()
polinomio2 = Polinomio()

print("Polinomio 1:", polinomio1.polinomio)
print("Polinomio 2:", polinomio2.polinomio)
