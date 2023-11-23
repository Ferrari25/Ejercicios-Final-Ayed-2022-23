
elemento = 8

class Cola:
    def __init__(self):
        self.frente = 1
        self.final = 1
        self.dato = [None] * elemento 
        
    def cola_vacia(self):
        if self.frente == self.final : 
            return True
        else:
            return print("la cola esta vacia")
    
    def cola_llena(self):
        siguiente = (self.final + 1) % elemento
        if siguiente == self.frente:
            return True
        else:
            print("la cola esta llena")
        
    def meter(self, valor):
        if not self.cola_llena():
            self.dato[self.final] = valor
            self.final = (self.final + 1) % elemento
        else: 
            print("la cola esta llena")

    def sacar(self):
        if not self.cola_vacia(): 
            valor = self.dato[self.frente]
            self.frente = (self.frente + 1) % elemento
            return valor
        else: 
            print("la cola esta vacia") 
    
    def mostrar(self):
        for i in range(self.frente,self.final):
            print(self.dato[i])
        return

votro =""
valor = 0
obj_cola = Cola()

while votro != "n":
    operacion = input("Ingrese la operacion que desea realizar:  [a/q]")
    if operacion == "a":
        valor = int(input("Ingrese el valor a agregar: "))
        obj_cola.meter(valor)
    elif operacion == "q":
        obj_cola.sacar()
    else: 
        print("operacion incorrecta")
    votro = input("Desea realizar otra operacion? [s/n]")
    if votro != "s":
        break

# obj_cola.meter(1)
# print("meti 1")
# obj_cola.meter(2)
# print("meti 2")
# obj_cola.meter(3)
# print("meti 3")
# obj_cola.meter(4)
# print("meti 4")
# obj_cola.meter(5)
# print("meti 5")
# obj_cola.meter(6)
# print("meti 6")
# #obj_cola.meter(7)
# obj_cola.sacar()
# obj_cola.sacar()
# print("meti 7") 
# print("este es el frebte de la cola {}".format(obj_cola.frente))
# print("este es el final de la cola {}".format(obj_cola.final))
# print("ultima ejecucion")
# obj_cola.mostrar()