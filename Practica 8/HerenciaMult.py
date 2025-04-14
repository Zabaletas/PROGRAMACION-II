class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z
    def incrementaXZ(self):
        self.x = self.x + 1
        self.z = self.z + 1
    def incrementaZ(self):
        self.z = self.z + 1
class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z
    def incrementaYZ(self):
        self.y = self.y + 1
        self.z = self.z + 1    
    def incrementaZ(self):
        self.z = self.z + 1
class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)    
    def incrementaXYZ(self):
        self.x = self.x + 1
        self.y = self.y + 1
        self.z = self.z + 1    
    def __str__(self):
        return f"(x={self.x}, y={self.y}, z={self.z})"
class Main:
    d = D(5, 10, 15)
    print(f"original: {d}")
    print("\nUsando los métodos de A:")
    d.incrementaXZ()
    print(f"Después de incrementaXZ: {d}")
    d.incrementaZ()
    print(f"Después de incrementaZ: {d}")
    print("\nUsando los métodos de B:")
    d.incrementaYZ()
    print(f"Después de incrementaYZ: {d}")
    d.incrementaZ()
    print(f"Después de incrementaZ: {d}")
    print("\nUsando el método de D:")
    d.incrementaXYZ()
    print(f"Después de incrementaXYZ: {d}")