class Interfaz:
    def __init__(self):
        self.polinomio = []

    def agregar_termino(self, coeficiente):
        self.polinomio.append(coeficiente)

    def modificar_termino(self, indice, nuevo_coeficiente):
        if indice >= 0 and indice < len(self.polinomio):
            self.polinomio[indice] = nuevo_coeficiente
        else:
            print("¡Índice inválido!")

    def obtener_valor(self, x):
        valor = 0
        for i in range(len(self.polinomio)):
            valor += self.polinomio[i] * (x ** i)
        return valor

