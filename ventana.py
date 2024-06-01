from customtkinter import *

FUENTE = "Arial"

class Pregunta:
    def __init__(self, app: CTk, label: str):
        self.label = CTkLabel(app, text=label, font=(FUENTE, 15, "bold"), fg_color="#242424", text_color="white")
        self.slider = CTkSlider(app, from_=0, to=10, command=None)

    def add(self, coordsX: int, coordY: int):
        self.label.place(x=coordsX, y=coordY)
        self.slider.place(x=coordsX + 400, y=coordY+8)


class Ventana(CTk):
    def __init__(self):
        super().__init__()
        self.main_frame = CTkFrame(self)
        self.geometry("800x800")

    def mostrar(self):
        self.mainloop()