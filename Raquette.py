'''
Class Raquette
Martin Timeo, Braz Arno
09/10/25
TODO : Faire une raquette de la bonne taille de manière à ne pas sortir la raquette de la zone de jeu
'''
import tkinter as tk

class palet:
    def __init__(self, canvas, x = 295, y=700, dim=(110, 15)):
        '''
        palet : un rectangle (canvas) représentant la plateforme que le joueur controle
        '''
        self.__canvas = canvas
        self.palet = self.__canvas.create_rectangle(x, y, x+dim[0], y+dim[1], fill="black")
        self.mur_d=405
        self.mur_g=295

    def droite(self):
        '''
        Déplace la raquette à droite à chaque pression de la flèche droite
        '''
        if self.mur_d <700:
            self.__canvas.move(self.palet, 20, 0)
            self.mur_d+=20
            self.mur_g+=20            
            # print(self.mur_d)

    def gauche(self):
        '''
        Déplace la raquette à gauche à chaque pression de la flèche gauche
        '''
        if self.mur_g >0:
            self.__canvas.move(self.palet, -20, 0)
            self.mur_g-=20
            self.mur_d-=20
            # print(self.mur_g)

#