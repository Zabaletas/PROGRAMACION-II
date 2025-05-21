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
# a. Crear dos pinturas con anuncios
artista3 = Artista("Da Vinci", "CI789", 25)
artista4 = Artista("Monet", "CI101", 15)
anuncio3 = Anuncio("A003", 6000)
anuncio4 = Anuncio("A004", 7000)

pintura1 = Pintura("Mona Lisa", "Óleo", artista3, anuncio=anuncio3, genero="Renacimiento")
pintura2 = Pintura("Impresión atardecer", "Acuarela", artista4, anuncio=anuncio4, genero="Impresionismo")
# b. Promedio de años de experiencia
def promedio_experiencia(pintura1, pintura2):
    artistas = []
    if pintura1.a1: artistas.append(pintura1.a1.añosExperiencia)
    if pintura1.a2: artistas.append(pintura1.a2.añosExperiencia)
    if pintura2.a1: artistas.append(pintura2.a1.añosExperiencia)
    if pintura2.a2: artistas.append(pintura2.a2.añosExperiencia)
    
    return sum(artistas) / len(artistas) if artistas else 0

promedio = promedio_experiencia(pintura1, pintura2)
print(f"Promedio de años de experiencia: {promedio}")
# c. Incrementar precio a pintura del artista X
def incrementar_precio_artista(pinturas, nombre_artista, incremento):
    for pintura in pinturas:
        if pintura.a1 and pintura.a1.nombre == nombre_artista and pintura.b:
            pintura.b.precio += incremento
        elif pintura.a2 and pintura.a2.nombre == nombre_artista and pintura.b:
            pintura.b.precio += incremento

incrementar_precio_artista([pintura1, pintura2], "Monet", 1000)
print(f"Nuevo precio de Monet: ${pintura2.b.precio}")