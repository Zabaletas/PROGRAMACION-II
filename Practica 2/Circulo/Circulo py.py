import tkinter as tk

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, root, centro, radio):
        self.centro = centro
        self.radio = radio
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.dibujar_circulo()

    def dibujar_circulo(self):
        self.canvas.create_oval(self.centro.x - self.radio, self.centro.y - self.radio,
                                self.centro.x + self.radio, self.centro.y + self.radio,
                                outline='black', width=2)

def main():
    root = tk.Tk()
    root.title("Dibujar Círculo")
    centro = Punto(200, 200)
    Circulo(root, centro, 50)
    root.mainloop()

if __name__ == "__main__":
    main()
