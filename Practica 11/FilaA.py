class Artista:
    def __init__(self, nombre, ci, añosExperiencia):
        self.nombre = nombre
        self.ci = ci
        self.añosExperiencia = añosExperiencia

class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

class Obra:
    def __init__(self, titulo, material, artista1, artista2=None, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.a1 = artista1
        self.a2 = artista2
        self.b = anuncio

class Pintura(Obra):
    def __init__(self, titulo, material, artista1, artista2=None, anuncio=None, genero=None):
        super().__init__(titulo, material, artista1, artista2, anuncio)
        self.genero = genero
# a. Crear objetos Pintura (con y sin anuncio)
artista1 = Artista("Van Gogh", "CI123", 20)
artista2 = Artista("Picasso", "CI456", 30)
anuncio1 = Anuncio("A001", 5000)

pintura_con_anuncio = Pintura("Noche estrellada", "Óleo", artista1, anuncio=anuncio1, genero="Impresionismo")
pintura_sin_anuncio = Pintura("Guernica", "Óleo", artista2, genero="Cubismo")
# b. Artista con más experiencia
def artista_mas_experiencia(pintura1, pintura2):
    artistas = []
    if pintura1.a1: artistas.append(pintura1.a1)
    if pintura1.a2: artistas.append(pintura1.a2)
    if pintura2.a1: artistas.append(pintura2.a1)
    if pintura2.a2: artistas.append(pintura2.a2)
    
    if not artistas:
        return None
    return max(artistas, key=lambda x: x.añosExperiencia).nombre

nombre_artista_experto = artista_mas_experiencia(pintura_con_anuncio, pintura_sin_anuncio)
print(f"Artista con más experiencia: {nombre_artista_experto}")
# c. Agregar anuncio y calcular monto total
anuncio2 = Anuncio("A002", 8000)
pintura_sin_anuncio.b = anuncio2

monto_total = pintura_con_anuncio.b.precio + pintura_sin_anuncio.b.precio
print(f"Monto total de venta: ${monto_total}")