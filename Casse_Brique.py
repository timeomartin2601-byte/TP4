'''
Casse-Brique : Programme principal
Braz Arno, Martin Timeo
16/10/25
TODO :  - Gestion des vies
        - Prévoir un bouton rejouer à la fin
        - Idéalement remplacer un max de forme par des images pour que ce soit plus beau et agréable à jouer
        -label rejouer,timer,vies,retour au menu
'''

# Importation des modules et des classes

import tkinter as tk
import Blocs
import Balle
import Raquette 
from tkinter import messagebox

# '''
# Section tirée d'internet permettant de résoudre un problème de dimension d'un écran à l'autre
# références utilisées : https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp?
# et https://stackoverflow.com/questions/62794931/high-dpi-tkinter-re-scaling-when-i-run-it-in-spyder-and-when-i-run-it-direct-in?
# '''
# try:
#     from ctypes import windll
#     windll.shcore.SetProcessDpiAwareness(1)  # Windows 8.1+
# except Exception:
#     pass


# Création de la fenêtre tkinter 

window = tk.Tk()
window.title('Casse-Brique')
window.geometry('700x800')
# window.attributes('-fullscreen', True)

frame_info = tk.Frame(window, width=700, height=800, bg='grey')
frame_info.pack(fill='both')

btn_close = tk.Button(frame_info, text="X", command=window.destroy)
btn_close.pack(side='right')

# Création du menu

frame_menu = tk.Frame(window, width=700, height=800)
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

    frame_canvas = tk.Frame(window, width=700, height=800)
    frame_canvas.pack(fill='both', expand=True)

    canvas = tk.Canvas(frame_canvas, bg='light grey', width=700, height=800)
    canvas.pack(fill='both')

    canvas.create_line(0, 0, 700, 0, fill='green', width=10)
    canvas.create_line(0, 0, 0, 800, fill='green', width=10)
    canvas.create_line(700, 0, 700, 800, fill='green', width=10)


    # Création des objets 
    raquette = Raquette.palet(canvas)
    balle = Balle.balle(canvas,)
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
    global canvas, balle, blocs, vies
    if blocs.vide():
        messagebox.showinfo(message='Bravo!')
        #TODO
        return
    idbloc = balle.id_col(canvas)
    if idbloc == -1:
        vies -= 1
        balle.del_balle(canvas)
        balle=Balle.balle(canvas)
        print(vies)
        if vies <= 0:
            messagebox.showinfo(message='Partie terminée !')
            # window.destroy()
            return
        window.after(1000, jeu)
        #TODO La gestion des vies
    else:
        if idbloc!= 0 and len(idbloc)>0:
            for obj in idbloc : 
                blocs.cassage(canvas, obj)
        balle.deplacement(canvas)
        window.after(10, jeu)


window.bind("<Key>", mouvement)
tk.mainloop()

