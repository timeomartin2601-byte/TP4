'''
Casse-Brique : Programme principal
Braz Arno, Martin Timeo
16/10/25
TODO :  - Gestion des vies
        - Prévoir un bouton rejouer à la fin
        - Idéalement remplacer un max de forme par des images pour que ce soit plus beau et agréable à jouer
        - label rejouer,timer,vies,retour au menu
'''

# Importation des modules et des classes

import tkinter as tk
import Blocs
import Balle
import Raquette 
import Menu
import Jeu
from tkinter import messagebox
from PIL import ImageTk

# Création de la fenêtre tkinter 


window = tk.Tk()
window.title('Casse-Brique')
largeur = window.winfo_screenwidth()
hauteur = window.winfo_screenheight()
window.geometry(f'700x800+{int((largeur/2)-350)}+{int((hauteur/2)-400)}')
window.overrideredirect(True)
# window.attributes('-fullscreen', True)

frame_info = tk.Frame(window, width=700, height=200, bg='grey')
frame_info.pack(fill='both')


btn_close = tk.Button(frame_info, text="X", command=window.destroy)
btn_close.pack(side='right')


def fenetre_menu():

    # Création du menu

    menu = Menu.lemenu(window)

    # Initialisation des variables globales
    canvas = None
    raquette = None
    balle = None
    blocs = None
    vies = 1
    diff = None

    def retour_menu():
        frame_canvas.destruction()
        fenetre_menu()
        
    def rejouer():
        initialisation()

    # Démarrage du jeu (à la pression du bouton Jouer)
    def initialisation():
        # Paramètrages des variables globales
        global canvas, raquette, balle, blocs, vies, diff, frame_canvas,parametre
        try:
            vies = menu.nb_vies()
            diff = menu.difficulte() 
            parametre=[vies,diff]
        except Exception as e:
            vies=parametre[0]
            diff=parametre[1]
            
        frame_canvas = Jeu.jeu(window, vies)
        canvas = frame_canvas.lecanvas()
        
        # Création des objets 
        raquette = Raquette.palet(canvas)
        balle = Balle.laballe(canvas, raquette.id_paletg(), raquette.id_paletd())
        blocs = Blocs.lesblocs(canvas, diff)
        
        jeu()

    b1 = tk.Button(menu.frame(), text='Jouer', command=initialisation)
    b1.pack()

    # Programme Principal

    def mouvement(event):
        global raquette
        if event.keysym == 'Left':
            raquette.gauche()

        if event.keysym == 'Right':
            raquette.droite()
    def stop(event):
        global raquette
        raquette.stop()

    def jeu():
        global canvas, raquette, balle, blocs, vies
        if blocs.vide():
            messagebox.showinfo(message='Bravo!')
            #TODO
            return
        idbloc = balle.id_col()
        if idbloc == -1:
            vies -= 1
            balle.del_balle()
            balle=Balle.laballe(canvas, raquette.id_paletg(), raquette.id_paletd())
            print(vies) #TODO Label
            if vies <= 0:
                frame_canvas.restart(retour_menu,rejouer,window)
                return
            window.after(1000, jeu)
            #TODO La gestion des vies
        else:
            if idbloc!= 0 and len(idbloc)>0:
                for obj in idbloc : 
                    blocs.cassage(obj)
            balle.deplacement()
            raquette.mouv()
            window.after(10, jeu)

    def rejouer():
        initialisation()


    window.bind("<KeyPress>", mouvement)
    window.bind("<KeyRelease>", stop)
    tk.mainloop()


fenetre_menu()