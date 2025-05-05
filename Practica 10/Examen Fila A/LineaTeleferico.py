class LineaTeleferico:
    def __init__(self, color="", tramo="", nro_cabinas=0, empleados=None, edades=None, sueldos=None):
        self.__color = color
        self.__tramo = tramo
        self.__nro_cabinas = nro_cabinas
        # Valores por defecto para empleados, edades y sueldos
        if empleados is None:
            self.__empleados = [
                ["pedro", "rojas", "luna"],
                ["lucy", "sosa", "rios"],
                ["ana", "perez", "rojas"],
                ["saul", "arce", "calle"]
            ]
        else:
            self.__empleados = empleados
        if edades is None:
            self.__edades = [35, 43, 26, 29]
        else:
            self.__edades = edades
        if sueldos is None:
            self.__sueldos = [2500.0, 3250.0, 2700.0, 2500.0]
        else:
            self.__sueldos = sueldos
        self.__nro_empleados = len(self.__empleados)
    def __str__(self):
        cad = (f"Color: {self.__color}, Tramo: {self.__tramo}, "
               f"Nro. Cabinas: {self.__nro_cabinas}, Nro. Empleados: {self.__nro_empleados}\n")
        cad += "Empleados:\n"
        for i in range(self.__nro_empleados):
            cad += (f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, "
                   f"Edad: {self.__edades[i]}, Sueldo: {self.__sueldos[i]}\n")
        return cad
    # Inciso b) Eliminar empleados por apellido (paterno o materno)
    def eliminar_por_apellido(self, apellido):
        i = 0
        while i < self.__nro_empleados:
            if (self.__empleados[i][1].lower() == apellido.lower() or 
                self.__empleados[i][2].lower() == apellido.lower()):
                # Eliminar empleado
                self.__empleados.pop(i)
                self.__edades.pop(i)
                self.__sueldos.pop(i)
                self.__nro_empleados -= 1
            else:
                i += 1
    # Inciso c) Sobrecarga del operador + para transferir empleados
    def __add__(self, otro):
        if not isinstance(otro, LineaTeleferico):
            raise TypeError("Solo se puede transferir entre objetos LineaTeleferico")
        if self.__nro_empleados == 0:
            return otro
        # Transferir el primer empleado
        empleado = self.__empleados[0]
        edad = self.__edades[0]
        sueldo = self.__sueldos[0]
        # Añadir al otro objeto
        otro.__empleados.append(empleado)
        otro.__edades.append(edad)
        otro.__sueldos.append(sueldo)
        otro.__nro_empleados += 1
        # Eliminar del objeto actual
        self.__empleados.pop(0)
        self.__edades.pop(0)
        self.__sueldos.pop(0)
        self.__nro_empleados -= 1
        
        return otro
    # Métodos auxiliares para inciso d)
    def obtener_mayor_edad(self):
        if self.__nro_empleados == 0:
            return -1
        return max(self.__edades)
    def obtener_mayor_sueldo(self):
        if self.__nro_empleados == 0:
            return -1.0
        return max(self.__sueldos)
    # Inciso d) Sobrecarga de métodos para mostrar empleados
    def mostrar(self, criterio: int):
        """Muestra empleados con mayor edad (criterio=1) o mayor sueldo (criterio=2)"""
        if criterio == 1:  # Mayor edad
            mayor_edad = self.obtener_mayor_edad()
            if mayor_edad == -1:
                print("No hay empleados para mostrar")
                return
            print("Empleados con mayor edad:")
            for i in range(self.__nro_empleados):
                if self.__edades[i] == mayor_edad:
                    print(f"{self.__empleados[i][0]} {self.__empleados[i][1]} - Edad: {self.__edades[i]}")
        elif criterio == 2:  # Mayor sueldo
            mayor_sueldo = self.obtener_mayor_sueldo()
            if mayor_sueldo == -1.0:
                print("No hay empleados para mostrar")
                return
            print("Empleados con mayor sueldo:")
            for i in range(self.__nro_empleados):
                if self.__sueldos[i] == mayor_sueldo:
                    print(f"{self.__empleados[i][0]} {self.__empleados[i][1]} - Sueldo: {self.__sueldos[i]}")
        else:
            print("Criterio no válido")
# Ejemplo de uso
if __name__ == "__main__":
    print("=== PRUEBA DE LINEA TELEFERICO ===")
    # Inciso a) Instanciar 2 objetos de diferente forma
    print("\n--- Creación de objetos ---")
    linea1 = LineaTeleferico(
        color="Rojo",
        tramo="Estación Central, Estación Cementerio, Estación 16 de Julio",
        nro_cabinas=20
    )
    linea2 = LineaTeleferico()  # Con valores por defecto    
    print("\nLínea 1:")
    print(linea1)
    
    print("\nLínea 2:")
    print(linea2)
    # Inciso b) Eliminar empleados por apellido
    print("\n--- Eliminar empleados con apellido 'Rojas' ---")
    linea1.eliminar_por_apellido("Rojas")
    linea2.eliminar_por_apellido("Rojas")
    
    print("\nLínea 1 después de eliminar:")
    print(linea1)
    
    print("\nLínea 2 después de eliminar:")
    print(linea2)
    # Inciso c) Transferir empleado (sobrecarga de operador +)
    print("\n--- Transferir empleado de Linea1 a Linea2 ---")
    linea2 = linea1 + linea2  # Transfiere un empleado de linea1 a linea2
    print("\nLínea 1 después de transferir:")
    print(linea1)
    
    print("\nLínea 2 después de transferir:")
    print(linea2)
    # Inciso d) Mostrar empleados con mayor edad y sueldo
    print("\n--- Empleados con mayor edad ---")
    linea1.mostrar(1)  # 1 para mayor edad
    
    print("\n--- Empleados con mayor sueldo ---")
    linea1.mostrar(2)  # 2 para mayor sueldo