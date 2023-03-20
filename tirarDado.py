from cProfile import label
from cgitb import text
from tkinter import *
import random

def tirar():
    dados = {1:'\u2680', 2:'\u2681', 3: '\u2682', 4:'\u2683', 5:'\u2684', 6:'\u2685'}
    numero_dado = random.randint(1,6)
    dado_obtenido = dados.get(numero_dado)
    etiDado.configure(text= dado_obtenido)
    etiNUmDado.configure(text= numero_dado)


ventana = Tk()
ventana.geometry("200x200") # ancho x alto
ventana.title("Dado")
btnTirar =Button(ventana, text="Tirar dado", command=tirar)
btnTirar.grid(column=1, row=0)

etiDado = Label(ventana, text= '\u2681', font=("Arial", 65))
etiDado.grid(column=2, row=1)

etiNUmDado = Label(ventana, text="2", font=("Arial", 20))
etiNUmDado.grid(column=3, row=1)

ventana.mainloop()