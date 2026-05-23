class Nodo:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None

class HashTable:

    def __init__(self, Q):
        self.capacity = Q
        self.size = 0
        self.table = [None] * Q

    def func_hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, val):
        idx = self.func_hash(key)

        if self.table[idx] is None:
            self.table[idx] = Nodo(key, val)
            self.size = self.size + 1
        else:
            actual = self.table[idx]
            while actual:
                if actual.key == key:
                    actual.value = val
                    return
                if actual.next is None:
                    break
                actual = actual.next
            actual.next = Nodo(key, val)
            self.size += 1

    def search(self, k):
        idx = self.func_hash(k)

        current = self.table[idx]
        while current:
            if current.key == k:
                return current.value
            current = current.next
        raise KeyError(k)

    def remove(self, key):
        idx = self.func_hash(key)

        prev = None
        current = self.table[idx]

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[idx] = current.next
                self.size = self.size - 1
                return
            prev = current
            current = current.next

        raise KeyError(key)

    def get_all_values(self):
        # este es un metodo auxiliar para sumar todos los valores (para TOTAL)
        total = 0
        for i in range(self.capacity):
            actual = self.table[i]
            while actual:
                total += actual.value
                actual = actual.next
        return total

def main():
    n = int(input())  # número de operaciones
    if not (1 <= n <= 1000):
        return
    ventas = HashTable(100) # se crea la tabla hash con capacidad 100

    for _ in range(n):
        partes = input().split()

        if partes[0] == "VENDER":
            producto = partes[1]
            cantidad = int(partes[2])

            if not (1 <= cantidad <= 1000):
                return

            # se intenta buscar el producto; si no existe, se empieza en 0
            try:
                cantidad_actual = ventas.search(producto)
            except KeyError:
                cantidad_actual = 0

            # se inserta o se actualiza con la suma
            ventas.insert(producto, cantidad_actual + cantidad)

        elif partes[0] == "CONSULTAR":
            producto = partes[1]

            # se intenta buscar; si no existe, se imprime 0
            try:
                print(ventas.search(producto))
            except KeyError:
                print(0)

        elif partes[0] == "TOTAL":
            # se suman todos los valores de la tabla hash
            print(ventas.get_all_values())

if __name__ == "__main__":
    main()
