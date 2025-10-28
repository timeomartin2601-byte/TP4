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
import Frame_Info
import Score
import Chrono
import Menufin
from tkinter import messagebox
from PIL import ImageTk

# Création de la fenêtre tkinter 


window = tk.Tk()
window.title('Casse-Brique')
largeur = window.winfo_screenwidth()
hauteur = window.winfo_screenheight()
window.geometry(f'700x800+{int((largeur/2)-350)}+{int((hauteur/2)-400)}')
# window.overrideredirect(True)
# window.attributes('-fullscreen', True)

frame_info = Frame_Info.info(window)

# frame_info = tk.Frame(window, width=700, height=200, bg='grey')

# frame_info.pack(fill='both')

# label_vies=tk.Label(frame_info, text='Nombre de vie : ',fg='white',bg='black')
# label_vies.pack(side='left')

# label_timer=tk.Label(frame_info, text='chrono : ',fg='white',bg='black')
# label_timer.pack(side='left')

# label_score=tk.Label(frame_info, text='score : ',fg='white',bg='black')
# label_score.pack(side='left')

# btn_close = tk.Button(frame_info, text="X", command=window.destroy)
# btn_close.pack(side='right')


# Initialisation des variables globales
canvas = None
raquette = None
balle = None
blocs = None
vies = 1
diff = None
final_time=None
score=0


def fenetre_menu():
    # Création du menu

    menu = Menu.lemenu(window)

    def retour_menu():
        if frame_info.btn_presents():
            frame_info.detruire()
        frame_canvas.destruction()
        fenetre_menu()

    # Démarrage du jeu (à la pression du bouton Jouer)
    def initialisation():
        # Paramètrages des variables globales
        global canvas, raquette, balle, blocs, vies, diff, frame_canvas,parametre,score,chrono
        
        if frame_info.btn_presents():
            frame_info.detruire()

        # Defini le nombre de vie et la difficulté et le garde en memoire en vue d'une nouvelle game sans passer par le menu principale
        if menu.existe():
            vies = menu.nb_vies()
            diff = menu.difficulte() 
            parametre=[vies,diff]
        else:
            vies=parametre[0]
            diff=parametre[1]
            
        
        frame_canvas = Jeu.jeu(window, vies)
        canvas = frame_canvas.lecanvas()

        #Affichage bouton 'retour menu' et 'rejouer'
        frame_info.restart(retour_menu,initialisation)
        # frame_canvas.restart(retour_menu,initialisation,frame_info)

        # Création des objets 
        raquette = Raquette.palet(canvas)
        balle = Balle.laballe(canvas, raquette.id_palet())
        blocs = Blocs.lesblocs(canvas, diff)
        score=Score.lescore()
        chrono=Chrono.lechrono()


        chrono.start_time()
        #rafraichie les labels 'label_vies' et 'label_timer'
        update()
        jeu()

    menu.jouer(initialisation)

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
        global canvas, raquette, balle, blocs, vies,final_time,chrono,score
        if blocs.vide():
            #Calcul du temps de jeu
            enregistrement_chrono()

            #calcul et memorisation du score final 
            enregistrement_score()

            #detruit le canvas de jeu et affiche le menu de fin 
            menu_fin('VICTOIRE')

            return
        idbloc = balle.id_col()
        if idbloc == -1:
            vies -= 1

            score.mort()
            update()
            
            balle.del_balle()
            balle=Balle.laballe(canvas, raquette.id_palet())

            if vies <= 0:
                #Calcul du temps de jeu (le chrono n'est pas enregistrer car le joueur a perdu)
                chrono.stop_time()

                #calcul et memorisation du score final 
                enregistrement_score()

                #detruit le canvas de jeu et affiche le menu de fin 
                menu_fin('GAME OVER')

                return
            window.after(1000, jeu)
        else:
            if idbloc!= 0 and len(idbloc)>0:
                for obj in idbloc : 
                    if blocs.cassage(obj)==True:
                        score.augmenter_score()
            update()
            balle.deplacement()
            raquette.mouv()
            window.after(10, jeu)

    window.bind("<KeyPress>", mouvement)
    window.bind("<KeyRelease>", stop)


    def update():
        #rafraichie les labels 'label_vies' et 'label_timer'
        global vies,chrono,blocs,score
        # label_vies.config(text='Nombre de vie : ' + str(vies))
        # label_timer.config(text='chrono : ' + str(round(chrono.le_chrono(), 2)) + 's')
        # label_score.config(text='score : ' + str(score.le_score()))
        frame_info.update_labels(vies, chrono.le_chrono(), score.le_score(chrono.le_chrono()))

    def menu_fin(message):
        #detruit le canvas de jeu et affiche le menu de fin 
        frame_canvas.destruction()
        menu_fin=Menufin.lemenu_fin(window,diff)
        menu_fin.text_titre(f'{message}')
        menu_fin.nbr_chrono(chrono.le_chrono())
        menu_fin.nbr_score(score.le_score(chrono.le_chrono()))
        menu_fin.restart(retour_menu,initialisation)

    def enregistrement_score():
        #calcul et enregistrement du score final 
        score.recup_donnée()
        score.historique_score(diff,chrono.le_chrono())
        score.classement_score(diff,chrono.le_chrono())
        score.memorisation()

    def enregistrement_chrono():
        #Calcul et enregistrement du chrono
        chrono.stop_time()
        chrono.recup_donnée()
        chrono.historique_chrono1(diff)
        chrono.classement_chrono1(diff)
        chrono.memorisation()

    tk.mainloop()


fenetre_menu()