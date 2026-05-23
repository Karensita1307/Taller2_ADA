class Queue:

    def __init__(self):
        self.head = 0 
        self.tail = -1
        self.e = []

    def enqueue(self,paciente):
        self.e.append(paciente)
        self.tail = self.tail + 1

    def dequeue(self):
        if len(self.e) == 0:
            return None
        else:
            v = self.e.pop(0)
            self.tail = self.tail - 1
            return v

    def first(self):
        return self.e[0]

    def last(self):
        return self.e[-1] # No usamos el metodo last(), pero lo dejamos por que asi lo puso Mateito <3

    def size(self): 
        return len(self.e) # Tampoco usamos el metodo size()

    def isEmpty(self):
        return len(self.e) == 0
    
def main():
    cola = Queue() # Para inicializar la cola de pacientes
    N = int(input()) # Cantidad de operaciones a realizar
    
    if 1 <= N <= 1000: #Se verifica el rango de N
        for _ in range(N):
            entrada = input().split() #Entrada que corresponde a la operación a realizar
            if entrada[0] == "LLEGA": # [0] Es el tipo de operación y [1] Es el nombre del paciente
                paciente = entrada[1]
                cola.enqueue(paciente)
            elif entrada[0] == "ATIENDE":
                if cola.isEmpty():
                    print("SIN PACIENTES")
                else:
                    print(cola.dequeue())
            elif entrada[0] == "SIGUIENTE":
                if cola.isEmpty():
                    print("COLA VACIA")
                else:
                    print(cola.first())
            else:                
                print("OPERACION INVALIDA")
    else:
        print("N FUERA DE RANGO") # Si se sale del rango de N para

if __name__ == "__main__":
    main()