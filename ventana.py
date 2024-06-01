from customtkinter import *
from classes import Comida
import vector

FUENTE = "Arial"

class Pregunta:
    def __init__(self, app: CTk, label: str):
        self.label = CTkLabel(app, text=label, font=(FUENTE, 15, "bold"), text_color="white")
        self.slider = CTkSlider(app, from_=0, to=10, command=None)

    def add(self, coordsX: int, coordY: int):
        self.label.place(x=coordsX, y=coordY)
        self.slider.place(x=coordsX + 400, y=coordY+8)


class LabelComida(CTkLabel):
    def __init__(self,
                app: CTk,
                text: str,
                fuente: tuple[str, int, str], 
                text_color=str
                ):
        super().__init__(app, text=text, font=fuente, text_color=text_color)

    def add(self, coordsX: int, coordY: int):
        self.place(x=coordsX, y=coordY)


class Ventana(CTk):
    def __init__(self, datos: list[str, int]):
        super().__init__()
        self.lista_recomendados: list[LabelComida] = []
        self.lista_preguntas: list[Pregunta] = []
        self.datos: list[str, int] = datos
        self.main_frame = CTkFrame(self)
        self.geometry("640x800")
        self.resizable(width=False, height=False)

    def add_pregunta(self, pregunta: Pregunta, coordX: int, coordY: int):
        pregunta.add(coordX, coordY)
        self.lista_preguntas.append(pregunta)
        
    def add_label_comida(self, label: LabelComida, coordX: int, coordY: int):
        label.add(coordX, coordY)
        self.lista_recomendados.append(label)

    def get_valores_preguntas(self) -> list[int]:
        return [pregunta.slider.get() for pregunta in self.lista_preguntas]
    
    def muesta_cercanos(self):
        label_resulados = CTkLabel(self,
                               font=(FUENTE, 20, "bold"),
                               text="Según tus preferencias, esto te podría gustar: "
                               )
        label_resulados.place(x=19, y=400)
        lista_cercanos = vector.ordena_cercanos(self.get_valores_preguntas(), self.datos)
        for i, v in enumerate(self.lista_recomendados):
            v.configure(text=f"{i + 1}: {lista_cercanos[i].nombre}")

    def mostrar(self):
        self.mainloop()