from Polinomio import polinomio1, polinomio2
# Función para obtener la longitud de un polinomio
def get_length(polinomio):
    return len(polinomio)
# Función para sumar dos polinomios
def sumar(polinomio1, polinomio2):
    resultado = []
    grado_max = max(len(polinomio1), len(polinomio2))
    for i in range(grado_max):
        coef1 = polinomio1[i] if i < len(polinomio1) else 0
        coef2 = polinomio2[i] if i < len(polinomio2) else 0
        suma = coef1 + coef2
        resultado.append(suma)
    return resultado

# Función para restar dos polinomios
def restar(polinomio1, polinomio2):
    resultado = []
    grado_max = max(len(polinomio1), len(polinomio2))
    for i in range(grado_max):
        coef1 = polinomio1[i] if i < len(polinomio1) else 0
        coef2 = polinomio2[i] if i < len(polinomio2) else 0
        resta = coef1 - coef2
        resultado.append(resta)
    return resultado

# Función para multiplicar dos polinomios
def multiplicar(polinomio1, polinomio2):
    grado_total = len(polinomio1) + len(polinomio2) - 1
    resultado = [0] * grado_total
    for i in range(len(polinomio1)):
        for j in range(len(polinomio2)):
            resultado[i + j] += polinomio1[i] * polinomio2[j]
    return resultado

# Función para dividir dos polinomios (no implementada aquí)
def dividir(polinomio1, polinomio2):
    # Aquí va la lógica para dividir polinomios
    grado_p1 = len(polinomio1) - 1
    grado_p2 = len(polinomio2) - 1

    if grado_p2 < 0:
        raise ValueError("El divisor no puede ser un polinomio constante cero")

    if grado_p1 < grado_p2:
        return [0], polinomio1

    cociente = [0] * (grado_p1 - grado_p2 + 1)
    residuo = polinomio1.copy()

    while grado_p1 >= grado_p2:
        coeficiente = residuo[grado_p1] / polinomio2[grado_p2]
        cociente[grado_p1 - grado_p2] = coeficiente

        for i in range(grado_p2 + 1):
            residuo[grado_p1 - grado_p2 + i] -= coeficiente * polinomio2[i]

        grado_p1 = len(residuo) - 1

    return cociente, residuo

# Función para mostrar un polinomio
def mostrar(polinomio):
    grado = len(polinomio) - 1
    resultado = ""
    for i, coef in enumerate(polinomio):
        if coef != 0:
            if i == 0:
                resultado += str(coef)
            else:
                resultado += f" + {coef}x^{i}"
    if resultado == "":
        resultado = "0"
    return resultado

print("Polinomio 1:",(polinomio1))
print("Polinomio 2:", (polinomio2))
print("Suma:",(sumar(polinomio1, polinomio2)))
print("Resta:",(restar(polinomio1, polinomio2)))
print("Multiplicación:", (multiplicar(polinomio1, polinomio2)))
print("División:", (dividir(polinomio1, polinomio2)))
print("Longitud del polinomio 1:", len(polinomio1))
print("Longitud del polinomio 2:", len(polinomio2))
