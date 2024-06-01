import db_connection as db
import vector
from classes import Comida

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


def main():
    db.create_table()

    datos = db.get_datos()

    comida = elegir_comida(datos)

    print("Elegiste:", comida.nombre)
    print("Esta es una lista de comida que pensamos que te puede gustar:")

    for i in ordena_cercanos(comida, datos)[0:6]:
        print(i.nombre)
    
    db.close()

main()