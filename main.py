import db_connection as db
import vector
from classes import Comida
from ventana import *

def elige_num(lo: int, hi: int, message: str) -> int:
    while True:
        print(message, end=" ")
        num = input()
        if num.isdigit():
            num = int(num)
            if num in range(lo, hi + 1):
                return num
        print(f"Introduce un número entre {lo} y {hi}.")

def elegir_comida(lista_comida: list[Comida]) -> Comida:
    for i, v in enumerate(lista_comida, 1):
        print(f"{i}: {v.nombre}")
    eleccion = elige_num(1, len(lista_comida), "Escribe el número con la opción que quieras:")
    return lista_comida[eleccion - 1]


def ordena_cercanos(objetivo: Comida, lista_comidas: list[Comida]) -> list[Comida]:
    return [i for i in sorted(lista_comidas, key=lambda c: vector.distancia(objetivo.vector, c.vector))]


def crearVentana() -> Ventana:
    app = Ventana()

    title = CTkLabel(app, font=(FUENTE, 30, "bold"), text="Buscador de comida con vectores")
    title.place(x=20, y=20)

    lista_labels = [
        "¿Qué importancia le das al valor nutricional?",
        "¿Qué tanto te importa el sabor?",
        "¿Cuánto te importa la textura en la comida?",
        "¿En qué nivel es importante la presentación para ti?",
        "¿Qué tanto te importa el tiempo de preparación?"
    ]

    for i, label in enumerate(lista_labels):
        Pregunta(app, label).add(20, 100 + 42*i)

    return app


def main():
    db.create_table()

    datos = db.get_datos()

    app = crearVentana()

    app.mostrar()
    
    db.close()

main()