'''
Casse-Brique : Programme principal
Braz Arno, Martin Timeo
16/10/25
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
window.overrideredirect(True)

#Creation du bandereau
frame_info = Frame_Info.info(window)

# Initialisation des variables globales
canvas = None
raquette = None
balle = None
blocs = None
vies = 1
diff = None
final_time=None
score=0
id_dernier_after = None


def fenetre_menu():
    ''' Création du menu, permet de recreer le Menu principale ultérieurement'''

    menu = Menu.lemenu(window)

    def retour_menu():
        ''' Renvoie le joueur au menu principal '''
        global id_dernier_after
        if id_dernier_after:
            window.after_cancel(id_dernier_after)
            id_dernier_after = None
        frame_info.detruire()
        frame_canvas.destruction()
        fenetre_menu()

    # Démarrage du jeu (à la pression du bouton Jouer)
    def initialisation():
        ''' Initialisation de la fenêtre de jeu, des paramètres et des objets '''

        # Paramètrages des variables globales
        global canvas, raquette, balle, blocs, vies, diff, frame_canvas, parametre, score, chrono, id_dernier_after
        
        if id_dernier_after:
            window.after_cancel(id_dernier_after)
            id_dernier_after = None

        if frame_info.btn_presents():
            frame_info.detruire()

        # Defini le nombre de vie et la difficulté et le garde en memoire en vue d'une nouvelle game sans passer par le menu principal
        if menu.existe():
            nombre_vies = menu.nb_vies()
            diff = menu.difficulte() 
            parametre=[nombre_vies, diff]
        else:
            nombre_vies=parametre[0]
            diff=parametre[1]
            
        vies = []
        for vie in range(nombre_vies):
            vies.append("vie")
        
        frame_canvas = Jeu.jeu(window, vies)
        canvas = frame_canvas.lecanvas()

        #Affichage bouton 'retour menu' et 'rejouer'
        frame_info.restart(retour_menu,initialisation)

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
        '''
        A la pression d'une flèche, on appelle les modifications de vitesse nécessaire à la raquette
        '''
        global raquette
        if event.keysym == 'Left':
            raquette.gauche()

        if event.keysym == 'Right':
            raquette.droite()

    def stop(event):
        '''
        Au relachement du bouton par le joueur, la fonction remet la vitesse de la raquette à 0
        '''
        global raquette
        raquette.stop()

    def jeu():
        '''
        Gestion des événements liés au jeu
        Sortie : None, arrêt du jeu
        '''
        global canvas, raquette, balle, blocs, vies, final_time, chrono, score, id_dernier_after

        chrono.time()
        chrono.le_chrono()

        if blocs.vide():
            #Calcul du temps de jeu
            enregistrement_chrono()

            #calcul et memorisation du score final 
            enregistrement_score()

            #detruit le canvas de jeu et affiche le menu de fin 
            frame_info.detruire()
            frame_canvas.destruction()
            menu_fin('VICTOIRE')

            return
        idbloc = balle.id_col()
        if idbloc == -1:
            vies.pop()

            score.mort()
            update()
            
            balle.del_balle()
            balle=Balle.laballe(canvas, raquette.id_palet())

            if vies == []:
                #Calcul du temps de jeu (le chrono n'est pas enregistrer car le joueur a perdu)
                chrono.time()
                chrono.le_chrono()

                #calcul et memorisation du score final 
                enregistrement_score()

                #detruit le canvas de jeu et affiche le menu de fin 
                frame_info.detruire()
                frame_canvas.destruction()
                menu_fin('GAME OVER')

                return
            id_dernier_after = window.after(1000, jeu)
        else:
            if idbloc!= 0 and len(idbloc)>0:
                for obj in idbloc : 
                    if blocs.cassage(obj)==True:
                        score.augmenter_score()
            update()
            balle.deplacement()
            raquette.mouv()
            id_dernier_after = window.after(10, jeu)

    window.bind("<KeyPress>", mouvement)
    window.bind("<KeyRelease>", stop)


    def update():
        ''' Rafraichie les labels 'label_vies' et 'label_timer' '''
        global vies,chrono,blocs,score
        frame_info.update_labels(len(vies), chrono.le_chrono(), score.le_score(chrono.le_chrono()))

    def menu_fin(message):
        ''' Detruit le canvas de jeu et affiche le menu de fin
            Parametre message : type str, Soit GAME OVER soit VICTOIRE
        ''' 
        frame_canvas.destruction()
        menu_fin=Menufin.lemenu_fin(window,diff)
        menu_fin.text_titre(f'{message}')
        menu_fin.nbr_chrono(chrono.le_chrono())
        menu_fin.nbr_score(score.le_score(chrono.le_chrono()))
        menu_fin.restart(retour_menu,initialisation)

    def enregistrement_score():
        ''' Calcul et enregistrement du score final '''
        score.recup_donnée()
        score.historique_score(diff,chrono.le_chrono())
        score.classement_score(diff,chrono.le_chrono())
        score.memorisation()

    def enregistrement_chrono():
        ''' Calcul et enregistrement du chrono '''
        chrono.time()
        chrono.le_chrono()
        chrono.recup_donnée()
        chrono.historique_chrono1(diff)
        chrono.classement_chrono1(diff)
        chrono.memorisation()

    tk.mainloop()


fenetre_menu()