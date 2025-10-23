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




def fenetre_menu():

    # Création du menu
    menu = Menu.lemenu(window)

    # Initialisation des variables globales
    canvas = None
    raquette = None
    balle = None
    blocs = None
    vies = 3
    diff = None


    # Démarrage du jeu (à la pression du bouton Jouer)
    def initialisation():
        # Paramètrages des variables globales
        global canvas, raquette, balle, blocs, vies, diff, frame_canvas
        vies = menu.nb_vies()
        diff = menu.difficulte() 

        frame_canvas = Jeu.jeu(window, vies)
        canvas = frame_canvas.lecanvas()
        
        canvas.bind("<KeyPress>", mouvement)
        canvas.bind("<KeyRelease>", stop)


        # Création des objets 
        raquette = Raquette.palet(canvas)
        balle = Balle.laballe(canvas, raquette.id_paletg(), raquette.id_paletd())
        blocs = Blocs.lesblocs(canvas, diff)
        
        jeu()

    b1 = tk.Button(menu.frame(), text='Jouer', command=initialisation)
    b1.pack()

    def retour_menu():
        frame_canvas.destruction()
        fenetre_menu()
    
    def rejouer():
        canvas.destroy()
        initialisation()
    
    # Programme Principal

    def mouvement(event):
        global canvas, raquette
        if event.keysym == 'Left':
            raquette.gauche()

        if event.keysym == 'Right':
            raquette.droite()

    def stop(event):
        global raquette
        raquette.stop()

    def jeu():
        global canvas, balle, blocs, vies, raquette
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
                # if retry:
                #     frame_canvas.frame().destroy()                  #TODO WIP rejouer
                # window.destroy()
                return
            window.after(1000, jeu)
            #TODO La gestion des vies
        else:
            if idbloc!= 0 and len(idbloc)>0:
                for obj in idbloc : 
                    blocs.cassage(obj)
            balle.deplacement()
            window.after(10, jeu)


    tk.mainloop()

fenetre_menu()