import math as m

def producto_interno(vec1: list[int], vec2: list[int]=None) -> float:
    # No hemos definido un producto interno todavía.

    if vec2 is None:
        vec2 = vec1[:]

    return sum(vec1[i] * vec2[i] for i in range(len(vec1)))


def norma(vec1: list[int]) -> float:
    return m.sqrt(producto_interno(vec1))


def multiplica(vec1: list[int], vec2: list[int]) -> int:
    if len(vec1) != len(vec2):
        raise Exception("Ambos vectores deben de tener la misma dimensión.")
    return sum(map(lambda x: x[0] * x[1], zip(vec1, vec2)))


def multiplica_escalar(escalar: float, vec: list[int]) -> int:
    return [escalar * i for i in vec]


def resta(vec1: list[int], vec2: list[int]) -> list[int]:
    if len(vec1) != len(vec2):
        raise Exception("Ambos vectores deben de tener la misma dimensión.")
    return [m.fabs(vec2[i] - vec1[i]) for i in range(len(vec1))]


def distancia(vec1: list[int], vec2: list[int]) -> float:
    return norma(resta(vec2, vec1))