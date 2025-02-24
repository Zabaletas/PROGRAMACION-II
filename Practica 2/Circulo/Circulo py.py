import tkinter as tk

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class CirculoDibujo(tk.Canvas):
    ESCALA = 20
    MARGEN = 25

    def __init__(self, master, centro, radio):
        super().__init__(master, width=500, height=500, bg="white")
        self.centro = centro
        self.radio = radio
        self.dibujar_circulo()

    def dibujar_circulo(self):
        ancho = int(self["width"])
        alto = int(self["height"])
        x_centro = ancho // 2 + self.centro.x * self.ESCALA
        y_centro = alto // 2 - self.centro.y * self.ESCALA
        r = self.radio * self.ESCALA
        self.create_oval(x_centro - r, y_centro - r, x_centro + r, y_centro + r, outline="black")

def main():
    root = tk.Tk()
    root.title("Dibujar Círculo")
    centro = Punto(0, 0)
    radio = 5
    canvas = CirculoDibujo(root, centro, radio)
    canvas.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
