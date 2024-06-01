import db_connection as db
from ventana import *

def crearVentana(datos: list[str, int]) -> Ventana:
    app = Ventana(datos)

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
        app.add_pregunta(Pregunta(app, label), 20, 100 + 42*i)

    boton_calcular = CTkButton(app,
                               command=app.muesta_cercanos,
                               text="Busca comidas similares",
                               fg_color="#09611f",
                               hover_color="#08300c",
                               width=300,
                               height=50
                            )
    
    boton_calcular.place(x=177, y=320)

    for i in range(5):
        app.add_label_comida(
            LabelComida(app, "", ("Arial", 15, "bold"), "white"),
            20,
            450 + 60 * i
            )

    return app


def main():
    db.create_table()

    datos = db.get_datos()

    app = crearVentana(datos)

    app.mostrar()
    
    db.close()

main()