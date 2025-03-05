class Cola:
    def __init__(self, n):
        self.n = n
        self.arreglo = [0] * n
        self.inicio = 0
        self.fin = -1
    
    def insert(self, e):
        if not self.isFull():
            self.fin += 1
            self.arreglo[self.fin] = e
    
    def remove(self):
        if not self.isEmpty():
            valor = self.arreglo[self.inicio]
            self.inicio += 1
            return valor
        return -1
    
    def peek(self):
        if not self.isEmpty():
            return self.arreglo[self.inicio]
        return -1
    
    def isEmpty(self):
        return self.inicio > self.fin
    
    def isFull(self):
        return self.fin == self.n - 1
    
    def size(self):
        return self.fin - self.inicio + 1
