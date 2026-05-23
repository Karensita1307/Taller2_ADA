# problema 1: editor de texto con deshacer

# esta es la clase con la estructura de pila, propuesta por el profe
class Stack:
    def __init__(self, top=-1):
        self.e = []
        self.tope = top

    def top(self):
        return self.e[self.tope]

    def push(self, x):
        self.e.append(x)
        self.tope = self.tope + 1

    def pop(self):
        v = self.e.pop(-1)
        self.tope = self.tope - 1
        return v

    def size(self):
        return self.tope + 1

    def isEmpty(self):
        return self.tope < 0

def main():
    n = int(input()) # esto lee lo que se escribe y lo convierte en un número entero
    pila = Stack() # aquí se crea una pila vacía (usando la clase stack) donde se van a guardar las palabras del texto en el orden en que se escriban

    for _ in range(n): # esto va a repetir n veces, es decir, por cada operación que llega en la entrada
        partes = input().split() # esto va a leer una línea completa como "ESCRIBIR hola" y la va a partir en pedacitos ("ESCRIBIR" y "hola"), donde parte[0] es el comando y parte[1] es la palabra, así se podrá revisar qué operación llega, y si hace falta, la palabra que vino con ella

# si la operación es ESCRIBIR, se mete la palabra en la pila con push
        if partes[0] == "ESCRIBIR":
            palabra = partes[1]
            pila.push(palabra)

# si la operación es DESHACER y la pila no está vacía, se quita la última con pop
        elif partes[0] == "DESHACER":
            if not pila.isEmpty():
                pila.pop()

# si la operación es MOSTRAR, se imprimen todas las palabras unidas por espacio o VACIO si no hay ninguna
        elif partes[0] == "MOSTRAR":
            if pila.isEmpty():
                print("VACIO")
            else:
                print(" ".join(pila.e)) # esta parte toma la lista de palabras como "hola", "mundo" y la convierte en el texto "hola mundo" para imprimirse en una sola línea

if __name__ == "__main__":
    main()