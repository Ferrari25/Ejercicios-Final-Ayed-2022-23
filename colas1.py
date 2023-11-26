
elementos = 6

class Cola:

    def __init__(self):
        self.frente = 1
        self.final = 1
        self.dato = [None] * elementos

        
    def cola_vacia(self):
        if self.frente == self.final : 
            return True

    
    def cola_llena(self):
        siguiente = (self.final % elementos) + 1
        if siguiente == self.frente:
            return True

        
    def meter(self, valor):
        if not self.cola_llena():
            self.dato[self.final] = valor
            self.final = (self.final % elementos) + 1
        else: 
            print("la cola esta llena")
        return
  

    def sacar(self):
        if not self.cola_vacia():   
            valor = self.dato[self.frente]
            self.frente = (self.frente % elementos) + 1
        else: print("la cola esta vacia")
        
        if (self.frente == elementos) and (self.final == elementos):
            self.frente = 1
            self.final = 1
            print("la cola se reinicio")
        return valor

    
    def mostrar(self):
        for i in range(self.frente,self.final):
            print(self.dato[i])
        return

votro =""
operacion = 0
valor = 0
obj_cola = Cola()


while votro != "n":
    print("1 - agregar elemento:  ")
    print("2 - sacar elemento:  ")
    print("3 - consultar cola:  ")
    operacion = int(input("elija una operacion: "))
    if operacion == 1:
        valor = int(input("Ingrese el valor a agregar:  "))
        obj_cola.meter(valor)
    elif operacion == 2:
        obj_cola.sacar()
    elif operacion == 3:
        obj_cola.mostrar()
    else:
        print("operacion incorrecta")
    votro = input("Desea realizar otra operacion? [s/n]:  ")
    if votro != "s":
        break
    
        
