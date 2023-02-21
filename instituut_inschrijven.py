from tkinter import *
import pikle_databank
from leerlingen import Leerlingen, Leerling


def global_num():
    global num
    num = 0


def incantator():
    if not leerling.indicator:
        leerling.indicator = True
        ja.config(bg='green')
    else:
        leerling.indicator = False
        ja.config(bg='white')


def ready():
    leerling.naam = naam.get()
    leerlingen.list.append(leerling)
    pikle_databank.save_leerlingen(leerlingen)
    canvas.quit()


def getikt(school):
    global num
    num += 1
    for x in range(0, len(list_button)):
        if list_button[x].cget('text') == school:
            list_button[x].config(text=str(num) + ".  " + school)
    leerling.list.append(school)


global_num()
kinderen = pikle_databank.load_leerlingen()
scools = pikle_databank.load_school()

leerlingen = Leerlingen()
leerlingen.list = kinderen.list

leerling = Leerling()

tk = Tk()
canvas = Canvas(tk, width=200, height=200)
canvas.pack()

list_button = [
    Button(tk, text='wawa', command=lambda: getikt("wawa")),
    Button(tk, text='koe', command=lambda: getikt("koe")),
    Button(tk, text='BCR colege', command=lambda: getikt("BCR colege")),
    Button(tk, text='vliegje', command=lambda: getikt("vliegje")),
    Button(tk, text='blork', command=lambda: getikt("blork")),
    Button(tk, text='ha hmmm', command=lambda: getikt("ha hmmm"))]

naam = StringVar()
naam.set('naam')
tekstvak = Entry(textvariable=naam)
ready = Button(tk, text='ready', command=ready)
ja = Button(tk, text='als je een indiecatorleerling bent klik dan hier', command=lambda: incantator())
ready.place(x=40, y=10)
ja.place(x=40, y=40)
tekstvak.place(x=40, y=70)

for x in range(0, len(list_button)):
    list_button[x].place(x=400, y=x*30)

tk.mainloop()
