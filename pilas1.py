elemento = 6

class Pila: 
    def __init__(self):
        self.cima = 0
        self.dato = [0] * elemento

    def pila_vacia(self):
        if self.cima == 0:
            return True

    def pila_llena(self):
        if self.cima == elemento - 1:
            return True

    def agregar(self, valor):
        if not self.pila_llena():
            self.cima += 1
            self.dato[self.cima] = valor
        else: 
            print("La pila esta llena")
        return

    def quitar(self):
        if not self.pila_vacia():
            self.cima -= 1
        else:
            print("La pila esta vacia")
        return 

    def mostrar(self):
        for i in range(self.cima,-1,-1 ): # para que muestre de manera correcta LIFO, arriba el ultima y ultimo el primero
            print(self.dato[i])
            
obj_pila = Pila()

valor = 0
votro = ""
voperacion = ""

while votro != "n":
    print("1 - agregar elemento:  ")
    print("2 - sacar elemento:  ")
    print("3 - consultar pila:  ")
    operacion = int(input("elija una operacion: "))
    if operacion == 1:
        valor = int(input("Ingrese el valor a agregar:  "))
        obj_pila.agregar(valor)
    elif operacion == 2:
        obj_pila.quitar()
    elif operacion == 3:
        obj_pila.mostrar()
    else:
        print("operacion incorrecta")
    votro = input("Desea realizar otra operacion? [s/n]:  ")
    if votro != "s":
        break



