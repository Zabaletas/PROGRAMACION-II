import tkinter as tk

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linea:
    def __init__(self, root, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.canvas = tk.Canvas(root, width=600, height=600, bg='white')
        self.canvas.pack()
        self.dibujar_linea()

    def dibujar_linea(self):
        escala = 70
        self.canvas.create_line(self.p1.x * escala, self.p1.y * escala,
                                self.p2.x * escala, self.p2.y * escala,
                                fill='pink', width=2)

def main():
    root = tk.Tk()
    root.title("Dibujar Línea")
    p1 = Punto(0, 0)
    p2 = Punto(3, 5)
    Linea(root, p1, p2)
    root.mainloop()

if __name__ == "__main__":
    main()
