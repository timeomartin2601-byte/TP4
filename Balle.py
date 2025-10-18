'''
Class Balle
Martin Timeo, Braz Arno
09/10/25
TODO : Fin du jeu pour y = 1080 et option de jeu sur les paramètres de vitesse
'''
import tkinter as tk
# from random import randint

class Balle : 
    def __init__(self, canvas, x=940, y=710, diametre=40):
        '''
        Création de la balle, sauvegarde de son identifiant, création de ses paramètres coordonnées et vitesse (Par défaut : balle 40x40 px)
        TODO : vitesse croissante et initialisation aléatoire par exemple
        '''
        self.__balle = canvas.create_oval(x, y, x+diametre, y+diametre, fill = "red")
        self.__rayon = diametre/2
        self.__x0, self.__y0, self.__x1, self.__y1 = canvas.coords(self.__balle)
        self.__vitx = -10
        self.__vity = -10

    def deplacement(self, canvas):
        '''
        Gére le déplacement de la balle, vérifie si il y a collision et réagis en conséquence
        Gestion :   - définir la délimitation de l'aire de jeu 
                    - inversion du x, y ou les 2 en fonction de la collision
        Sortie : int, l'identifiant de l'objet collisionné sinon 0
        '''
        id_bloc = 0
        self.__x0, self.__y0, self.__x1, self.__y1 = canvas.coords(self.__balle)
        

        haut = self.collision(canvas, (self.__x0+self.__x1)/2, self.__y0, (self.__x0+self.__x1)/2, self.__y0)
        bas = self.collision(canvas, (self.__x0+self.__x1)/2, self.__y1, (self.__x0+self.__x1)/2, self.__y1)
        if (haut + bas > 0 ) or self.collision_hori(canvas) : 
            self.__vity = -self.__vity
            id_bloc = haut + bas

        gauche = self.collision(canvas, self.__x0, (self.__y0+self.__y1)/2, self.__x0, (self.__y0+self.__y1)/2)
        droite = self.collision(canvas, self.__x1, (self.__y0+self.__y1)/2, self.__x1, (self.__y0+self.__y1)/2)
        if (gauche + droite > 0) or self.collision_lat(canvas) : 
            self.__vitx = -self.__vitx
            id_bloc = gauche + droite

        # centre_balle = (self.__x0+self.__x1)/2 
        # diag1 = self.collision(canvas, centre_balle-self.__rayon, centre_balle+self.__rayon, centre_balle+self.__rayon, centre_balle-self.__rayon)
        # diag2 = self.collision(canvas, centre_balle-self.__rayon, centre_balle-self.__rayon, centre_balle+self.__rayon, centre_balle+self.__rayon)
        # if (diag1 + diag2 > 0) : 
        #     print('les diags', diag1, diag2)
        #     self.__vitx, self.__vity = -self.__vitx, -self.__vity
        #     id_bloc = gauche + droite

        canvas.move(self.__balle, self.__vitx, self.__vity) 
        return id_bloc
    
    def collision_hori(self, canvas):
        '''
        Detecte si il y a collision avec un bloc (ou la raquette) ou avec la bordure y = 0 (TODO si y = 1080 : fin de la partie) 
        Sortie : bool, True si il y a eu collision False sinon 
        '''
        return self.__y0 == 0 or self.__y1 == 1080

    def collision_lat(self, canvas):
        '''
        Detecte si il y a collision avec l'une des bordures x = 0 ou x = 1920
        Sortie : bool, True si il y a eu collision False sinon 
        '''
        return self.__x0 == 0 or self.__x1 == 1920
    
    def collision(self, canvas, x1, y1, x2, y2):
        '''
        Detecte si il y a collision avec l'une des bordures x = 0 ou x = 1920
        Sortie : int, id de l'objet collisionné (0 sinon) 
        TODO : Possibilité de toucher plusieurs objets en même temps
        '''
        overlap = canvas.find_overlapping(x1, y1, x2, y2)
        if overlap != tuple() and 52 in overlap: 
            print(overlap)
        if overlap != tuple():
            for id_obj in overlap:
                if id_obj != self.__balle:
                    return id_obj
        return 0