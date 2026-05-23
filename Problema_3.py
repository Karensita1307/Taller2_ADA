class Nodo:
    def __init__(self, k):
        self.key = k
        self.next = None


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begin(self, x):
        n = Nodo(x)
        n.next = self.head
        self.head = n

    def insert_at_end(self, x):
        n = Nodo(x)
        if self.head is None:
            self.head = n
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = n

    def insert(self, pos, x): # Agregamos insert para insertar la canción en la posicion dada
        if pos == 0: # Insertar al inicio en caso que la posición sea 0
            self.insert_at_begin(x)
            return
        
        n = Nodo(x)
        t = self.head
        i = 0
        while t.next and i < pos - 1: # Avanzar hasta la posicion anterior
            t = t.next
            i += 1
        n.next = t.next
        t.next = n

    def delete_from_begin(self): # No usamos eliminar el primer elemento en este caso
        if self.head is None:
            return "Vacia"
        self.head = self.head.next

    def delete_from_end(self): # Tampoco usamos eliminar el último elemento
        if self.head is None:
            return "Vacia"
        if self.head.next is None:
            self.head = None
        else:
            t = self.head
            while t.next.next:
                t = t.next
            t.next = None
    
    def delete(self, x): # Mejor creamos Eliminar la canción por nombre
        if self.head is None:
            return
        
        if self.head.key == x: # Si esta al inicio
            self.head = self.head.next
            return
        
        t = self.head # Sino la buscamos en el resto de la lista
        while t.next:
            if t.next.key == x:
                t.next = t.next.next
                return
            t = t.next

    def succesor(self, x): # No usamos en este caso ésta función
        n = self.search(x)
        if n != None:
            return n.next.key
        return "no existe"

    def print_list(self):
        if self.head is None:
            print("LISTA VACIA")
            return
        t = self.head
        while t:
            print(t.key, end=' ')
            t = t.next
        print()

    def search(self, x): # Tampoco usamos esta función
        current = self.head
        while current:
            if current.key == x:
                return current
            current = current.next
        return None


def main():
    lista = SingleLinkedList() # Creamos la lista de reproducción :)
    N = int(input())

    if 1 <= N <= 1000: # Hacemos el rango
        for _ in range(N):
            x = input().split()
            if x[0] == "AGREGAR":
                lista.insert_at_end(x[1])
            elif x[0] == "INSERTAR":
                posicion = int(x[1])
                lista.insert(posicion, x[2])
            elif x[0] == "ELIMINAR":
                lista.delete(x[1])
            elif x[0] == "MOSTRAR":
                lista.print_list()
    else:
        print("N debe estar entre 1 y 1000")

if __name__ == "__main__":
    main()