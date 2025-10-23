'''
Casse-Brique : Programme principal
Braz Arno, Martin Timeo
16/10/25
TODO :  - Gestion des vies
        - Prévoir un bouton rejouer à la fin
        - Idéalement remplacer un max de forme par des images pour que ce soit plus beau et agréable à jouer
        - label timer,vies
'''

# Importation des modules et des classes

import time as time
import tkinter as tk
import Blocs
import Balle
import Raquette 
import Menu
import Jeu
from tkinter import messagebox

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

label_vies=tk.Label(frame_info, text='Nombre de vie : ',fg='white',bg='black')
label_vies.pack(side='left')

label_timer=tk.Label(frame_info, text='chrono : ',fg='white',bg='black')
label_timer.pack(side='left')

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
    final_time=None

    def retour_menu():
        frame_canvas.destruction()
        fenetre_menu()
        
    def rejouer():
        initialisation()

    # Démarrage du jeu (à la pression du bouton Jouer)
    def initialisation():
        # Paramètrages des variables globales
        global canvas, raquette, balle, blocs, vies, diff, frame_canvas,parametre,start_time
        try:
            vies = menu.nb_vies()
            diff = menu.difficulte() 
            parametre=[vies,diff]
        except:
            vies=parametre[0]
            diff=parametre[1]
            
        frame_canvas = Jeu.jeu(window, vies)
        canvas = frame_canvas.lecanvas()

        # Création des objets 
        raquette = Raquette.palet(canvas)
        balle = Balle.laballe(canvas, raquette.id_paletg(), raquette.id_paletd())
        blocs = Blocs.lesblocs(canvas, diff)
        
        start_time = time.perf_counter()

        update()
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
        global canvas, raquette, balle, blocs, vies,final_time,start_time
        if blocs.vide():
            messagebox.showinfo(message='Bravo!')
            #TODO
            return
        idbloc = balle.id_col()
        if idbloc == -1:
            vies -= 1

            update()
            
            balle.del_balle()
            balle=Balle.laballe(canvas, raquette.id_paletg(), raquette.id_paletd())
            print(vies) #TODO Label
            if vies <= 0:
                #Calcul du temps de jeu
                end_time = time.perf_counter()
                final_time = end_time - start_time
                print(f"Program executed in: {final_time: .5f} seconds")

                #Affichage bouton 'retour menu' et 'rejouer'
                frame_canvas.restart(retour_menu,rejouer,frame_info)
                return
            window.after(1000, jeu)
            #TODO La gestion des vies
        else:
            if idbloc!= 0 and len(idbloc)>0:
                for obj in idbloc : 
                    blocs.cassage(obj)
            update()
            balle.deplacement()
            raquette.mouv()
            window.after(10, jeu)

    window.bind("<KeyPress>", mouvement)
    window.bind("<KeyRelease>", stop)


    def update():
        global vies,start_time
        label_vies.config(text='Nombre de vie : ' + str(vies))
        label_timer.config(text='chrono : ' + str(round(time.perf_counter() - start_time, 2)) + 's')


    tk.mainloop()


fenetre_menu()