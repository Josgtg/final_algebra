class Comida:
    def __init__(self, data: list[str, int]):
        self.nombre = data[0]
        self.vector = data[1:]