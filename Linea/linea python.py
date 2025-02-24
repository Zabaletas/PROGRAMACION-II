Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
... 
... class Punto:
...     def _init_(self, x, y):
...         self.x = x
...         self.y = y
... 
... class Linea:
...     def _init_(self, p1, p2):
...         self.p1 = p1
...         self.p2 = p2
...         self.ventana = tk.Tk()
...         self.ventana.title("Dibujar Línea")
...         self.ventana.resizable(False, False)
...         self.canvas = tk.Canvas(self.ventana, width=600, height=600, bg="white")
...         self.canvas.pack()
...         self.dibujar_linea()
...         self.ventana.mainloop()
... 
...     def dibujar_linea(self):
...         self.canvas.create_line(self.p1.x * 70, self.p1.y * 70,
...                                 self.p2.x * 70, self.p2.y * 70, fill="pink", width=2)
... 
... class Circulo:
...     def _init_(self, centro, radio):
...         self.centro = centro
...         self.radio = radio
...         self.ventana = tk.Tk()
...         self.ventana.title("Dibujar Círculo")
...         self.ventana.resizable(False, False)
...         self.canvas = tk.Canvas(self.ventana, width=1000, height=1000, bg="white")
...         self.canvas.pack()
...         self.dibujar_circulo()
...         self.ventana.mainloop()
... 
    def dibujar_circulo(self):
        self.canvas.create_oval(self.centro.x * 10 - self.radio * 10, self.centro.y * 10 - self.radio * 10,
                                 self.centro.x * 10 + self.radio * 10, self.centro.y * 10 + self.radio * 10,
                                 outline="pink", width=2)

if _name_ == "_main_":
    p1 = Punto(3, 3)
    p2 = Punto(6, 6)
    Linea(p1, p2)
    
    centro = Punto(20, 20)
    radio = 7.5
