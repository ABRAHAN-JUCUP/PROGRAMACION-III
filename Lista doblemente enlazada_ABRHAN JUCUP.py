import graphviz

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo
        self.generar_grafo()

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.fin is None:
            self.fin = nuevo_nodo
            self.inicio = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.fin
            self.fin = nuevo_nodo
        self.generar_grafo()

    def eliminar_por_valor(self, carnet):
        actual = self.inicio
        while actual is not None:
            if actual.carnet == carnet:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente

                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.fin = actual.anterior
                self.generar_grafo()
                return True
            actual = actual.siguiente
        return False

    def mostrar_lista(self):
        actual = self.inicio
        while actual is not None:
            print(f"{actual.nombre} {actual.apellido} - Carnet: {actual.carnet} <-> ", end="")
            actual = actual.siguiente
        print("None")

    def generar_grafo(self):
        dot = graphviz.Digraph(comment='Lista Doblemente Enlazada')
        actual = self.inicio
        while actual is not None:
            dot.node(str(actual.carnet), f"{actual.nombre} {actual.apellido} ({actual.carnet})")
            if actual.anterior is not None:
                dot.edge(str(actual.anterior.carnet), str(actual.carnet))
            if actual.siguiente is not None:
                dot.edge(str(actual.carnet), str(actual.siguiente.carnet))
            actual = actual.siguiente
        dot.render('lista_doblemente_enlazada', format='png', cleanup=True)

def menu():
    print("Seleccione una opción:")
    print("1. Insertar al principio")
    print("2. Insertar al final")
    print("3. Eliminar por valor")
    print("4. Mostrar lista")
    print("5. Salir")

lista = ListaDoblementeEnlazada()

while True:
    menu()
    opcion = input("Opción: ")

    if opcion == '1':
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        carnet = input("Ingrese carnet: ")
        lista.insertar_al_principio(nombre, apellido, carnet)
    elif opcion == '2':
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        carnet = input("Ingrese carnet: ")
        lista.insertar_al_final(nombre, apellido, carnet)
    elif opcion == '3':
        carnet = input("Ingrese el carnet a eliminar: ")
        if lista.eliminar_por_valor(carnet):
            print("Nodo eliminado exitosamente.")
        else:
            print("No se encontró el carnet en la lista.")
    elif opcion == '4':
        print("Lista:")
        lista.mostrar_lista()
    elif opcion == '5':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
