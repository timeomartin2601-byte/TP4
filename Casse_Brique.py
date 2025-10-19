'''
Casse-Brique : Programme principal
Braz Arno, Martin Timeo
16/10/25
TODO :  - assembler les différentes classes ensemble
        - ajouter des paramètres de jeu
        - idéalement remplacer un max de forme par des images pour que ce soit plus beau et agréable à jouer
'''

# Importation des modules et des classes

import tkinter as tk
import Blocs
import Copie_Balle
import Raquette 
from tkinter import messagebox

# Création de la fenêtre tkinter 

window = tk.Tk()
window.title('Casse-Brique')
window.geometry('1920x1080')
window.attributes('-fullscreen', True)

# Création des sous-fenêtres et du bouton fermer TODO ajouter une frame pour les paramètres de jeu
frame_info = tk.Frame(window, width=1920, height=20, bg='grey')
frame_info.pack(fill='both', expand=True)

frame_canvas = tk.Frame(window, width=1920, height=1060)
frame_canvas.pack(fill='both', expand=True)

btn_close = tk.Button(frame_info, text="X", command=window.destroy)
btn_close.pack(side='right')

# Création du Canvas
canvas = tk.Canvas(frame_canvas, bg='light grey', width=1920, height=1060)
canvas.pack(fill='both')

canvas.create_line(0, 0, 1920, 0, fill='green', width=10)
canvas.create_line(0, 0, 0, 1060, fill='green', width=10)
canvas.create_line(1920, 0, 1920, 1060, fill='green', width=10)

canvas.create_line(0, 1050, 1920, 1050, fill='red', width=10)

# TODO Création d'un menu (button etc)


# Création des objets 
raquette = Raquette.palet(canvas)
balle = Copie_Balle.balle(canvas)
blocs = Blocs.blocs(canvas)

# Programme Principal

def mouvement(event):
    if event.keysym == 'Left':
        raquette.gauche(canvas)
    if event.keysym == 'Right':
        raquette.droite(canvas)

def jeu():
    if blocs.vide():
        messagebox.showinfo(message='Bravo!')
        return

    idbloc = balle.id_col(canvas)
    if idbloc == -1:
        balle.del_balle(canvas)
        window.destroy()
        #TODO
    else:
        blocs.cassage(canvas, idbloc)
        balle.deplacement(canvas)
        window.after(20, jeu)

jeu()

window.bind("<Key>", mouvement)
tk.mainloop()

