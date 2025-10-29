'''
Class Blocs
Martin Timeo, Braz Arno
09/10/25
'''
import tkinter as tk

class lesblocs:

    def __init__(self, canvas, etat = 1): 
        """
        Entrée : etat - int, réglable de 1 à 3 nombre de coups pour casser un bloc
        blocs : list, l'entièreté des identifiants des blocs 
        """
        self.__canvas = canvas
        blocs = dict()
        for l in range(8):
            for c in range(5):
                blocs[self.__canvas.create_rectangle(5 + (87 * l), 22 + (60 * c), 87 + (87 * l), 74 + (60 * c), fill="#1066B6")] = etat 
        self.__blocs = blocs


    def cassage(self, id_rect : int):
        """
        Supprime un bloc sur le canvas à partir de son identifiant et le supprime de la liste des blocs
        """
        couleurs = [None, 'red', 'orange']
        if id_rect in self.__blocs :
            self.__blocs[id_rect] -= 1
            etat = self.__blocs[id_rect]
            if etat > 0:
                self.__canvas.itemconfig(id_rect, fill=couleurs[etat])
            else:
                self.__canvas.delete(id_rect)
                del self.__blocs[id_rect]
                return True        

    def vide(self):
        '''
        Renvoie si il a plus de blocs
        Sortir : Bool, True il n'y a plus de blocs False sinon
        '''
        return self.__blocs == {}
    


