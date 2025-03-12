import math
class FiguraGeometrica:
    
    def area(self, radio):
        return math.pi * radio * radio  # Círculo
    def area(self, base, altura):
        return base * altura  # Rectángulo
    def area(self, base, altura, hipotenusa):
        return (base * altura) / 2  # Triángulo rectángulo
    def area(self, baseMenor, baseMayor, altura, inclinacion):
        return ((baseMenor + baseMayor) * altura) / 2  # Trapecio
    def area(self, lado, apotema, radio, perimetro, tipo):
        return (5 * lado * apotema) / 2  # Pentágono

if __name__ == "__main__":
    f1 = FiguraGeometrica()
    f2 = FiguraGeometrica()
    f3 = FiguraGeometrica()
    f4 = FiguraGeometrica()
    f5 = FiguraGeometrica()
    print("Círculo:", f1.area(1))
    print("Rectángulo:", f2.area(2, 3))
    print("Triángulo Rectángulo:", f3.area(3, 5, 7))
    print("Trapecio:", f4.area(2, 5, 7, 9))
    print("Pentágono:", f5.area(2, 3, 6, 7, 9))