'''
Class Raquette
Martin Timeo, Braz Arno
09/10/25
'''
import tkinter as tk

class palet:
    def __init__(self, canvas, x = 295, y=700, dim=(110, 15)):
        '''
        palet : un rectangle (canvas) représentant la plateforme que le joueur controle
        '''
        self.palet = canvas.create_rectangle(x, y, x+dim[0], y+dim[1], fill="black")
        self.mur_d=405
        self.mur_g=295

    def droite(self, canvas):
        '''
        Déplace la raquette à droite à chaque pression de la flèche droite
        '''
        if self.mur_d <700:
            canvas.move(self.palet, 20, 0)
            self.mur_d+=20
            self.mur_g+=20            
            # print(self.mur_d)

    def gauche(self, canvas):
        '''
        Déplace la raquette à gauche à chaque pression de la flèche gauche
        '''
        if self.mur_g >0:
            canvas.move(self.palet, -20, 0)
            self.mur_g-=20
            self.mur_d-=20
            # print(self.mur_g)
