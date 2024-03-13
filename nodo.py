class nodo:
    def __init__(self, info):
        self.info = info
        self.siguiente = None

# Load a set of words
polinomio1 = input("Ingrese los coeficientes del polinomio 1 separados por espacios: ").split()
polinomio1 = [int(coeficiente) for coeficiente in polinomio1]

polinomio2 = input("Ingrese los coeficientes del polinomio 2 separados por espacios: ").split()
polinomio2 = [int(coeficiente) for coeficiente in polinomio2]

# Create a linked list of nodes for polinomio1
head1 = None
for coeficiente in polinomio1:
    node = nodo(coeficiente)
    if head1 is None:
        head1 = node
    else:
        aux = head1
        while aux.siguiente is not None:
            aux = aux.siguiente
        aux.siguiente = node

# Create a linked list of nodes for polinomio2
head2 = None
for coeficiente in polinomio2:
    node = nodo(coeficiente)
    if head2 is None:
        head2 = node
    else:
        aux = head2
        while aux.siguiente is not None:
            aux = aux.siguiente
        aux.siguiente = node

# List the coefficients in the linked list for polinomio1
aux = head1
while aux is not None:
    print(aux.info)
    aux = aux.siguiente

# List the coefficients in the linked list for polinomio2
aux = head2
while aux is not None:
    print(aux.info)
    aux = aux.siguiente
