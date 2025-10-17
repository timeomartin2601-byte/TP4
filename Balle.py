'''
Class Balle
Martin Timeo, Braz Arno
09/10/25
todo : detection de collision ici ? 
'''
import tkinter as tk

# from random import randint

class Balle : 
    def __init__(self, canvas):
        self.__balle = canvas.create_oval(940, 710, 980, 750, fill = "red")
        self.__x = canvas.coords(self.__balle)[0]
        self.__y = canvas.coords(self.__balle)[1]
        self.__vitx = -10
        self.__vity = -10

    def deplacement(self, canvas):
        '''
        Gére le déplacement de la balle, vérifie si il y a collision et réagis en conséquence
        TODO :  - définir la délimitation de l'aire de jeu 
                - choisir une trajectoire de départ
                - inversion du y à chaque collision (sauf si collision latéral)
        '''
        self.__x = canvas.coords(self.__balle)[0]
        self.__y = canvas.coords(self.__balle)[1]
        if self.collision_hori(canvas): # TODO collision -> Bool ? Coord ? les 2 ? Type de collision (latéral ou horizontal)
            self.__vity = -self.__vity
        if self.collision_lat(canvas): # TODO collision -> Bool ? Coord ? les 2 ? Type de collision (latéral ou horizontal)
            self.__vitx = -self.__vitx

        canvas.move(self.__balle, self.__vitx, self.__vity) 

    def collision_hori(self, canvas):
        '''
        Detecte si il y a collision avec un bloc (ou la raquette) ou avec la bordure y = 0 (si y = 1080 : fin de la partie)
        Si la coord y de la balle est inférieur à y = 350 (blocs le + bas) : on appelle bloc de cassage (comment faire car autre class ?)
        '''
        if canvas.find_overlapping(self.__x, self.__y, self.__x, self.__y):
            return True
        return canvas.coords(self.__balle)[1] == 0 or canvas.coords(self.__balle)[3] == 1080 

    def collision_lat(self, canvas):
        '''
        Detecte si il y a collision avec un bloc (ou la raquette) ou avec l'une des bordures x = 0 ou x = 1920
        Si la coord y de la balle est inférieur à y = 350 (blocs le + bas) : on appelle bloc de cassage (comment faire car autre class?)
        '''
        if canvas.find_overlapping(self.__x, self.__y, self.__x, self.__y):
            return True
        return canvas.coords(self.__balle)[0] == 0 or canvas.coords(self.__balle)[2] == 1920