import tkinter as tk
import Blocs as blc
import raquette as pal
import Balle as bal

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)  # Windows 8.1+
except Exception:
    pass


# Création de la fenêtre

mw = tk.Tk()
mw.title("Casse Brique")
mw.geometry('1920x1080')
mw.attributes('-fullscreen', True)

# Création du Canvas

canvas = tk.Canvas(mw, bg='ivory', width=1920, height=1080)
canvas.grid(row=0, column=0, ipadx=1920, ipady=1080)
bord_g = canvas.create_line(0, 0, 0, 1080, width=5, fill='red')
bord_d = canvas.create_line(1920, 0, 1920, 1080, width=5, fill='red')

tk.Button(canvas, text="Quitter", command=mw.destroy).grid(row=0, column=2, ipadx=100, padx=750)

l = tk.Label(canvas, text="Nbr vies :", bg="red") # TODO Ajouter la var du nbr de vie 
l.grid(row=0, column=0, ipadx=100, padx=0)

l2 = tk.Label(canvas, text="Nbr vies :", bg="red") # TODO Ajouter la var du nbr de vie 
l2.grid(row=0, column=1, ipadx=100, padx=10)




# Création des Blocs
B = blc.Blocs(canvas)
balle = bal.Balle(canvas)

def on_key(event):
    if event.keysym == "space":
        balle.deplacement(canvas)
        B.cassage(canvas, coord=(220, 30))
    if event.keysym == "space" :
        canvas.move(blocs[(120, 30)], 300, 300)
        canvas.delete(blocs[(220, 30)])

def destr(event):
    rect = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    for rectangle in rect:
        canvas.delete(rectangle)

mw.bind("<Key>", on_key)
mw.bind("<Button-1>", destr)
    

    
#Creation palet
palet=pal.palet(canvas)

def mouv(event):
    if event.keysym == "Right":
        palet.droite(canvas)
    if event.keysym == "Left":
        palet.gauche(canvas)

mw.bind("<Key>", mouv)

mw.resizable(False, False)


tk.mainloop()
