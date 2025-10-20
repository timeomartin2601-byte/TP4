'''
Class Balle
Martin Timeo, Braz Arno
09/10/25
TODO : Collisions diagonales + Fin du jeu pour y = 1080 (+ option de jeu sur les paramètres de vitesse)
'''
import tkinter as tk
from random import randint

class balle : 
    def __init__(self, canvas, x=330, y=380, diametre=40): 
        '''
        Création de la balle, sauvegarde de son identifiant, création de ses paramètres coordonnées et vitesse (Par défaut : balle 40x40 px)
        TODO : vitesse croissante et initialisation aléatoire par exemple
        '''
        self.__balle = canvas.create_oval(x, y, x+diametre, y+diametre, fill = "red")
        self.__rayon = diametre/2 #-> non ?
        self.__x0, self.__y0, self.__x1, self.__y1 = canvas.coords(self.__balle)
        self.__vitx = randint(1, 10) * ((-1)**(randint(1, 2)))
        self.__vity = -10

    def id_col(self, canvas):
        '''
        Gére le déplacement de la balle, vérifie si il y a collision et réagis en conséquence
        Gestion :   - définir la délimitation de l'aire de jeu 
                    - inversion du x, y ou les 2 en fonction de la collision
        Sortie : int, l'identifiant de l'objet collisionné sinon 0
        TODO : Gestion des collisions diagonales 
        '''
        if self.perdu(canvas):
            return -1

        id_bloc = []
        self.__x0, self.__y0, self.__x1, self.__y1 = canvas.coords(self.__balle)
        
        haut = self.collision(canvas, (self.__x0+self.__x1)/2, self.__y0, (self.__x0+self.__x1)/2, self.__y0)
        bas = self.collision(canvas, (self.__x0+self.__x1)/2, self.__y1, (self.__x0+self.__x1)/2, self.__y1)
        if len(haut + bas)>0:
            self.__vity = -self.__vity
            id_bloc += haut + bas

        gauche = self.collision(canvas, self.__x0, (self.__y0+self.__y1)/2, self.__x0, (self.__y0+self.__y1)/2)
        droite = self.collision(canvas, self.__x1, (self.__y0+self.__y1)/2, self.__x1, (self.__y0+self.__y1)/2)
        if len(droite + gauche)>0:
            self.__vitx = -self.__vitx
            id_bloc += gauche + droite
        if id_bloc==[]:
            return 0
        return id_bloc
        
    def deplacement(self, canvas):
        if not self.arret(canvas):
            canvas.move(self.__balle, self.__vitx, self.__vity)
    
    def perdu(self, canvas):
        '''
        Detecte si il y a collision avec un bloc (ou la raquette) ou avec la bordure y = 0 (TODO si y = 1080 : fin de la partie) 
        Sortie : bool, True si il y a eu collision False sinon 
        '''
        if self.__y1 == 790:
            canvas.move(self.__balle,0,380)
            return True
        return False
    
    def collision(self, canvas, x1, y1, x2, y2):
        '''
        Detecte si il y a collision avec l'une des bordures x = 0 ou x = 700
        Sortie : int, id de l'objet collisionné (0 sinon) 
        TODO : Possibilité de toucher plusieurs objets en même temps
        '''
        ids=[]
        overlap = canvas.find_overlapping(x1, y1, x2, y2)
        for id_obj in overlap:
            if id_obj != self.__balle:
                ids.append(id_obj)
        return ids
    
    def del_balle(self, canvas):
        '''
        Détruit la balle 
        '''
        canvas.delete(self.__balle)

    def arret(self, canvas):
        '''
        Retourne si le jeu peut continuer ou non selon si la balle est encore présente 
        Sortie : Bool, True si le jeu doit s'arreter, False sinon
        '''
        return not self.__balle in canvas.find_all()