import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

# Clases de boletos
class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero
    
    @abstractmethod
    def obtener_precio(self):
        pass
    
    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.obtener_precio():.1f}"

class Palco(Boleto):
    def obtener_precio(self):
        return 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion
    
    def obtener_precio(self):
        return 50.0 if self.dias_anticipacion >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion
    
    def obtener_precio(self):
        return 25.0 if self.dias_anticipacion >= 10 else 30.0

# Interfaz gráfica
class TeatroMunicipalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal - Sistema de Boletos")
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tipo de boleto
        ttk.Label(main_frame, text="Tipo de boleto:").grid(row=0, column=0, sticky=tk.W)
        self.tipo_boleto = tk.StringVar()
        tipos = ["Palco", "Platea", "Galeria"]
        self.tipo_menu = ttk.Combobox(main_frame, textvariable=self.tipo_boleto, values=tipos, state="readonly")
        self.tipo_menu.grid(row=0, column=1, sticky=(tk.W, tk.E))
        self.tipo_menu.current(0)
        
        # Número de boleto
        ttk.Label(main_frame, text="Número de boleto:").grid(row=1, column=0, sticky=tk.W)
        self.numero_boleto = tk.IntVar()
        ttk.Entry(main_frame, textvariable=self.numero_boleto).grid(row=1, column=1, sticky=(tk.W, tk.E))
        
        # Días de anticipación
        self.dias_label = ttk.Label(main_frame, text="Días de anticipación:")
        self.dias_entry = ttk.Entry(main_frame)
        
        # Mostrar/ocultar días según selección
        self.tipo_boleto.trace_add('write', self.toggle_dias_anticipacion)
        
        # Botones
        ttk.Button(main_frame, text="Obtener Boleto", command=self.obtener_boleto).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(main_frame, text="Salir", command=self.root.quit).grid(row=4, column=0, columnspan=2)
        
        # Configurar expansión
        for child in main_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
    
    def toggle_dias_anticipacion(self, *args):
        if self.tipo_boleto.get() in ["Platea", "Galeria"]:
            self.dias_label.grid(row=2, column=0, sticky=tk.W)
            self.dias_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))
        else:
            self.dias_label.grid_forget()
            self.dias_entry.grid_forget()
    
    def obtener_boleto(self):
        try:
            numero = self.numero_boleto.get()
            tipo = self.tipo_boleto.get()
            
            if tipo == "Palco":
                boleto = Palco(numero)
            elif tipo == "Platea":
                dias = int(self.dias_entry.get())
                boleto = Platea(numero, dias)
            elif tipo == "Galeria":
                dias = int(self.dias_entry.get())
                boleto = Galeria(numero, dias)
            
            messagebox.showinfo("Información del Boleto", str(boleto))
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TeatroMunicipalApp(root)
    root.mainloop()