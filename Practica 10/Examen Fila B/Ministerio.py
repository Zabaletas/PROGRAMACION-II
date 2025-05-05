class Ministerio:
    # Clase interna para representar empleados (Inciso a - Estructura alternativa)
    class Empleado:
        def __init__(self, nombre, apellido_p, apellido_m, edad, sueldo):
            self.nombre = nombre
            self.apellido_p = apellido_p
            self.apellido_m = apellido_m
            self.edad = edad
            self.sueldo = sueldo
        
        def __str__(self):
            return f"{self.nombre} {self.apellido_p} {self.apellido_m}"
    # Constructor para inciso a)
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.empleados = [] 
    # Inciso a) Método estático para crear objetos de diferente forma
    @staticmethod
    def crear_objetos():
        # Objeto 1
        min1 = Ministerio("Medio Ambiente", "Av. Arce #1234")
        min1.empleados = [
            min1.Empleado("Pedro", "Rojas", "Luna", 35, 2500),
            min1.Empleado("Lucy", "Sosa", "Ríos", 43, 3250),
            min1.Empleado("Ana", "Perez", "Rojas", 26, 2700),
            min1.Empleado("Saul", "Arce", "Calle", 29, 2500)
        ]
        # Objeto 2
        min2 = Ministerio("Educación", "Av. 6 de Agosto #5678")
        min2.empleados = [
            min2.Empleado("Juan", "Gomez", "Perez", 40, 3000),
            min2.Empleado("Maria", "Lopez", "Garcia", 35, 2800)
        ]
        return min1, min2
    # Inciso b) Eliminar empleados con edad X
    def eliminar_empleados_edad(self, edad):
        self.empleados = [e for e in self.empleados if e.edad != edad]
    # Inciso c) Sobrecarga de operador para transferir empleado
    def __sub__(self, otro_ministerio):
        if self.empleados:
            # Transfiere el último empleado
            otro_ministerio.empleados.append(self.empleados.pop())
    # Inciso d) Mostrar empleados con menor edad
    def mostrar_empleados_menor_edad(self):
        if not self.empleados:
            print("No hay empleados")
            return
        min_edad = min(e.edad for e in self.empleados)
        print(f"Empleados con menor edad ({min_edad} años):")
        for emp in filter(lambda e: e.edad == min_edad, self.empleados):
            print(emp)
    # Inciso d) Mostrar empleados con menor sueldo
    def mostrar_empleados_menor_sueldo(self):
        if not self.empleados:
            print("No hay empleados")
            return
        min_sueldo = min(e.sueldo for e in self.empleados)
        print(f"Empleados con menor sueldo ({min_sueldo}):")
        for emp in filter(lambda e: e.sueldo == min_sueldo, self.empleados):
            print(emp)
# Ejemplo de uso con comentarios de incisos
if __name__ == "__main__":
    # Inciso a) Crear objetos
    min1, min2 = Ministerio.crear_objetos()
    # Inciso b) Eliminar empleados con edad 35
    min1.eliminar_empleados_edad(35)
    min2.eliminar_empleados_edad(35)
    # Inciso c) Transferir empleado usando sobrecarga de operador
    min2 - min1  # Transfiere de min2 a min1
    # Inciso d) Mostrar resultados
    min1.mostrar_empleados_menor_edad()
    min1.mostrar_empleados_menor_sueldo()