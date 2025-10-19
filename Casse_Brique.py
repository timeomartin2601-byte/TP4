'''
Casse-Brique : Programme principal
Braz Arno, Martin Timeo
16/10/25
TODO :  - Gestion des vies
        - Prévoir un bouton rejouer à la fin
        - Idéalement remplacer un max de forme par des images pour que ce soit plus beau et agréable à jouer
'''

# Importation des modules et des classes

import tkinter as tk
import Blocs
import Balle
import Raquette 
from tkinter import messagebox

# Création de la fenêtre tkinter 

window = tk.Tk()
window.title('Casse-Brique')
window.geometry('1920x1080')
window.attributes('-fullscreen', True)

frame_info = tk.Frame(window, width=1920, height=20, bg='grey')
frame_info.pack(fill='both')

btn_close = tk.Button(frame_info, text="X", command=window.destroy)
btn_close.pack(side='right')

# Création du menu

frame_menu = tk.Frame(window, width=1920, height=1060)
frame_menu.pack(fill='both', expand=True)

tk.Label(frame_menu, text='Jeu du Casse-Brique !', height=5).pack()

tk.Label(frame_menu, text='Nombre de vie (3 par défaut) :').pack()
vies_entry = tk.Entry(frame_menu)
vies_entry.pack()

tk.Label(frame_menu, text='difficulté (1 à 3) :').pack()
diff_entry = tk.Entry(frame_menu)
diff_entry.pack()

def entier(valeur):
    if valeur != '':
        for elt in valeur :
            if elt not in '0123456789':
                return False
        return True
    else:
        return False

# Initialisation des variables globales
canvas = None
raquette = None
balle = None
blocs = None
vies = 3 
diff = 1 

# Démarrage du jeu (à la pression du bouton Jouer)
def initialisation():
    # Paramètrages des variables globales
    global canvas, raquette, balle, blocs, vies, diff
    
    if entier(vies_entry.get()):
        vies = int(vies_entry.get())
    
    if diff_entry.get() in ['1', '2', '3']: 
        diff = int(diff_entry.get())

    # Création du canvas
    frame_menu.destroy()

    frame_canvas = tk.Frame(window, width=1920, height=1060)
    frame_canvas.pack(fill='both', expand=True)

    canvas = tk.Canvas(frame_canvas, bg='light grey', width=1920, height=1060)
    canvas.pack(fill='both')

    canvas.create_line(0, 0, 1920, 0, fill='green', width=10)
    canvas.create_line(0, 0, 0, 1060, fill='green', width=10)
    canvas.create_line(1920, 0, 1920, 1060, fill='green', width=10)

    # Création des objets 
    raquette = Raquette.palet(canvas)
    balle = Balle.balle(canvas)
    blocs = Blocs.blocs(canvas, diff)
    
    jeu()

b1 = tk.Button(frame_menu, text='Jouer', command=initialisation)
b1.pack()

# Programme Principal

def mouvement(event):
    global canvas, raquette
    if event.keysym == 'Left':
        raquette.gauche(canvas)
    if event.keysym == 'Right':
        raquette.droite(canvas)

def jeu():
    global canvas, balle, blocs
    if blocs.vide():
        messagebox.showinfo(message='Bravo!')
        #TODO
        return

    idbloc = balle.id_col(canvas)
    if idbloc == -1:
        balle.del_balle(canvas)
        window.destroy()
        #TODO La gestion des vies
    else:
        blocs.cassage(canvas, idbloc)
        balle.deplacement(canvas)
        window.after(20, jeu)


window.bind("<Key>", mouvement)
tk.mainloop()

