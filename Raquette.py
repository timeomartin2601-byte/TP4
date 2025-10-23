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
        self.__x, self.__y, self.__dim = x, y, dim
        self.__paletg = self.__canvas.create_rectangle(x, y, x+(dim[0]/2), y+dim[1], fill="black")
        self.__paletd = self.__canvas.create_rectangle(x+(dim[0]/2), y, x+dim[0], y+dim[1], fill="red")
        self.__mur_d=405
        self.__mur_g=295

    def droite(self):
        '''
        Déplace la raquette à droite à chaque pression de la flèche droite
        '''
        if self.__mur_d <700:
            self.__x += 20
            self.__mur_d+=20
            self.__mur_g+=20            
            # print(self.mur_d)

    def gauche(self):
        '''
        Déplace la raquette à gauche à chaque pression de la flèche gauche
        '''
        if self.__mur_g >0:
            self.__x -= 20
            self.__mur_g-=20
            self.__mur_d-=20
            # print(self.mur_g)

    def mouv(self):
        '''
        
        '''
        self.__canvas.coords(self.__paletg, self.__x, self.__y, self.__x+(self.__dim[0]/2), self.__y+self.__dim[1])
        self.__canvas.coords(self.__paletd, self.__x+(self.__dim[0]/2), self.__y, self.__x+self.__dim[0], self.__y+self.__dim[1])

    def id_paletg(self):
        '''
        
        '''
        return self.__paletg
    
    def id_paletd(self):
        '''
        
        '''
        return self.__paletd