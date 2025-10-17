'''
Class Balle
Martin Timeo, Braz Arno
09/10/25
TODO : Detecter les collisions latérales 
'''
import tkinter as tk

# from random import randint

class Balle : 
    def __init__(self, canvas):
        self.__balle = canvas.create_oval(940, 710, 980, 750, fill = "red") # id 51
        print(self.__balle)
        self.__xmin, self.__ymin, self.__xmax, self.__ymax = canvas.coords(self.__balle)
        self.__vitx = -10
        self.__vity = -10

    def deplacement(self, canvas):
        '''
        Gére le déplacement de la balle, vérifie si il y a collision et réagis en conséquence
        Sortie : int, l'id_rectangle si il y a collision sinon 0
        TODO :  - définir la délimitation de l'aire de jeu 
                - choisir une trajectoire de départ
                - inversion du y à chaque collision (sauf si collision latéral)
        '''
        sortie = 0
        self.__xmin, self.__ymin, self.__xmax, self.__ymax = canvas.coords(self.__balle)

        id_hori = self.collision_hori(canvas)
        if id_hori > 0 : 
            self.__vity = -self.__vity
            sortie = id_hori

        id_lat = self.collision_lat(canvas)
        if id_lat > 0: 
            self.__vitx = -self.__vitx
            sortie = id_lat

        canvas.move(self.__balle, self.__vitx, self.__vity) 
        if sortie > 0:
            print(sortie)
        return sortie

    def collision_hori(self, canvas):
        '''
        Detecte si il y a collision avec un bloc (ou la raquette) ou avec la bordure y = 0 (TODO si y = 1080 : fin de la partie)
        Si la coord y de la balle est inférieur à y = 350 (blocs le + bas) : on appelle bloc de cassage (comment faire car autre class ?)
        Sortie : int, l'id_rectangle (0 si il n'y a pas de collision 0 n'étant pas un id valide)   
        '''
        overlap = canvas.find_overlapping(self.__xmin, self.__ymin, self.__xmin, self.__ymin)
        if overlap != tuple() : 
            # print('sans', canvas.find_overlapping(self.__xmin, self.__ymin, self.__xmin, self.__ymin))
            # print('avec', canvas.find_overlapping(self.__xmin, self.__ymin, self.__xmax, self.__ymax))
            return overlap[0]
        return int(self.__ymin == 0 or self.__ymax == 1080)

    def collision_lat(self, canvas):
        '''
        Detecte si il y a collision avec un bloc (ou la raquette) ou avec l'une des bordures x = 0 ou x = 1920
        Si la coord y de la balle est inférieur à y = 350 (blocs le + bas) : on appelle bloc de cassage (comment faire car autre class?)
        '''
        overlap = canvas.find_overlapping(self.__xmin, self.__ymin, self.__xmin, self.__ymin)
        # if overlap != tuple() :
        #     return overlap[0]
        return int(self.__xmin == 0 or self.__xmax == 1920)