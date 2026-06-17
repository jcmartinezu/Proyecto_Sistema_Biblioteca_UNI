class Libro:
    def __init__(self, codigo, titulo, autor, disponible=True):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "autor": self.autor,
            "disponible": self.disponible
        }