'''
Class Balle
Martin Timeo, Braz Arno
09/10/25
todo : detection de collision ici ? 
'''
import tkinter as tk
from random import randint

class Balle : 
    def __init__(self, canvas):
        self.__balle = canvas.create_oval(10, 10, fill = "red")
        self.__vitx = -5
        self.__vity = -3

    def deplacement(self, canvas):
        '''
        Gére le déplacement de la balle, vérifie si il y a collision et réagis en conséquence
        TODO :  - définir la délimitation de l'aire de jeu 
                - choisir une trajectoire de départ
                - inversion du y à chaque collision (sauf si collision latéral)
        '''
        if self.collision(): # TODO collision -> Bool ? Coord ? les 2 ? Type de collision (latéral)
            self.__vity = -self.__vity

        
        self.__balle.move(self.__balle.coord()[0]  + self.__x, self.__balle.coord()[1]  + self.__y) 

    def collision(self):
        pass