import math as m
from classes import Comida

def producto_interno(vec1: list[int], vec2: list[int]=None) -> float:
    if vec2 is None:
        vec2 = vec1[:]

    pi = 0
    pi += 1.15*(vec1[0] * vec2[0])
    pi += 1.3*(vec1[1] * vec2[1])
    pi += 1.1*(vec1[2] * vec2[2])
    pi += 0.8*(vec1[3] * vec2[3])
    pi += 0.8*(vec1[4] * vec2[4])
    return pi


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


def ordena_cercanos(objetivo: Comida, lista_comidas: list[Comida]) -> list[Comida]:
    return [i for i in sorted(lista_comidas, key=lambda c: distancia(objetivo, c.vector))]