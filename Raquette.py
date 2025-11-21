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
        self.__canvas = canvas
        self.__x, self.__y, self.__dim = x, y, dim
        self.__palet = self.__canvas.create_rectangle(x, y, x+dim[0], y+dim[1], fill="red")
        self.__depl = 0

    def droite(self):
        '''
        Associe le nombre de pixel de deplacement à effectuer au prochain mouvement
        '''
        self.__depl = 10

    def gauche(self):
        '''
        Associe le nombre de pixel de deplacement à effectuer au prochain mouvement
        '''
        self.__depl = -10

    def stop(self):
        '''
        Supprime le déplacement de la balle (la balle s'arrête)
        '''
        self.__depl = 0

    def mouv(self):
        '''
        Déplace la raquette
        '''
        if self.__x + self.__depl > 0 and self.__x + self.__dim[0] + self.__depl < 700 :
            self.__x+=self.__depl

        self.__canvas.coords(self.__palet, self.__x, self.__y, self.__x+self.__dim[0], self.__y+self.__dim[1])
    
    def id_palet(self):
        '''
        Renvoie l'identifiant canvas du palet
        '''
        return self.__palet