'''
Class Balle
Martin Timeo, Braz Arno
09/10/25
TODO : Collisions diagonales + Fin du jeu pour y = 1080 (+ option de jeu sur les paramètres de vitesse)
'''
import tkinter as tk
from random import randint

class laballe : 
    def __init__(self, canvas, pg, pd, x=330, y=380, diametre=20): 
        '''
        Création de la balle, sauvegarde de son identifiant, création de ses paramètres coordonnées et vitesse (Par défaut : balle 40x40 px)
        TODO : vitesse croissante et initialisation aléatoire par exemple
        '''
        self.__pg, self.__pd = pg, pd
        self.__canvas = canvas
        self.__balle = self.__canvas.create_oval(x, y, x+diametre, y+diametre, fill = "red")
        self.__rayon = diametre/2 #-> non ?
        self.__x0, self.__y0, self.__x1, self.__y1 = self.__canvas.coords(self.__balle)
        # self.__vitx = randint(4, 8) * ((-1)**(randint(1, 2)))
        # self.__vity = -(9-abs(self.__vitx))
        self.__vitx = 5
        self.__vity = -5

    def id_col(self):
        '''
        Gére le déplacement de la balle en testant les axes X et Y séparemment
        pour éviter les fausses détections diagonales.
        '''
        if self.perdu():
            return -1
        
        self.__x0, self.__y0, self.__x1, self.__y1 = self.__canvas.coords(self.__balle)
        
        futur_y0 = self.__y0 + self.__vity
        futur_y1 = self.__y1 + self.__vity
        ids_vertical = self.collision(self.__x0, futur_y0, self.__x1, futur_y1)
        
        futur_x0 = self.__x0 + self.__vitx
        futur_x1 = self.__x1 + self.__vitx
        ids_horizontal = self.collision(futur_x0, self.__y0, futur_x1, self.__y1)

        id_bloc = []

        if len(ids_vertical) > 0:
            if self.__pg in ids_vertical:
                if self.__vitx > 0:
                    self.__vitx = -self.__vitx
            elif self.__pd in ids_vertical:
                if self.__vitx < 0:
                    self.__vitx = -self.__vitx
            self.__vity = -self.__vity
            id_bloc += ids_vertical

        if len(ids_horizontal) > 0:
            self.__vitx = -self.__vitx
            id_bloc += ids_horizontal
        
        if id_bloc == []:
            return 0
        
        return id_bloc
        
    def deplacement(self):
        if not self.arret():
            self.__canvas.move(self.__balle, self.__vitx, self.__vity)
    
    def perdu(self):
        '''
        Detecte si il y a collision avec un bloc (ou la raquette) ou avec la bordure y = 0 (TODO si y = 1080 : fin de la partie) 
        Sortie : bool, True si il y a eu collision False sinon 
        '''
        if self.__y1 == 790:
            self.__canvas.move(self.__balle,0,-380)
            return True
        return False
    
    def collision(self, x1, y1, x2, y2):
        '''
        Detecte si il y a collision avec l'une des bordures x = 0 ou x = 700
        Sortie : int, id de l'objet collisionné (0 sinon) 
        TODO : Possibilité de toucher plusieurs objets en même temps
        '''
        ids=[]
        overlap = self.__canvas.find_overlapping(x1, y1, x2, y2)
        for id_obj in overlap:
            if id_obj != self.__balle:
                ids.append(id_obj)
        return ids
    
    def del_balle(self):
        '''
        Détruit la balle 
        '''
        self.__canvas.delete(self.__balle)

    def arret(self):
        '''
        Retourne si le jeu peut continuer ou non selon si la balle est encore présente 
        Sortie : Bool, True si le jeu doit s'arreter, False sinon
        '''
        return not self.__balle in self.__canvas.find_all()
    
