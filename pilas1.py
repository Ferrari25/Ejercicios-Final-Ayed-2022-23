elemento = 6

class Pila: 
    def __init__(self):
        self.cima = 0
        self.dato = [0] * elemento

    def pila_vacia(self):
        return self.cima == 0

    def pila_llena(self):
        return self.cima == elemento -1

    def agregar(self, valor):
        if not self.pila_llena():
            self.cima += 1
            self.dato[self.cima] = valor
        else: print("la pila esta llena capo")
        return

    def quitar(self):
        if not self.pila_vacia():
            self.cima -= 1
        else: print("la pila esta vacia capo")
        return 

    def mostrar(self):
        for i in range(self.cima,-1,-1 ): # para que muestre de manera correcta LIFO, arriba el ultima y ultimo el primero
            print(self.dato[i])
            
obj_pila = Pila()

valor = 0
votro = ""
voperacion = ""

while votro != "n":
    operacion = input("Ingrese la operacion que desea realizar:  [a/q]")
    if operacion == "a":
        valor = int(input("Ingrese el valor a agregar: "))
        obj_pila.agregar(valor)
    elif operacion == "q":
        obj_pila.quitar()
    else: 
        print("operacion incorrecta")
    votro = input("Desea realizar otra operacion? [s/n]")
    if votro != "s":
        break

# obj_pila.agregar(1)
# obj_pila.agregar(2)
# obj_pila.agregar(3)
# obj_pila.agregar(4)
# obj_pila.agregar(5)
# obj_pila.agregar(6)
# obj_pila.agregar(7)
# obj_pila.agregar(8)
# obj_pila.quitar()
# obj_pila.mostrar()
