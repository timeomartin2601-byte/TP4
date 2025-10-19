'''
Class Blocs
Martin Timeo, Braz Arno
09/10/25
'''
import tkinter as tk

class Blocs:
    def __init__(self, canvas, etat): 
        """
        Entrée : etat - int, réglable de 1 à 3 nombre de coups pour casser un bloc
        blocs : list, l'entièreté des identifiants des blocs 
        """
        blocs = dict()
        for l in range(10):
            for c in range(5):
                blocs[canvas.create_rectangle(10 + (190 * l), 30 + (80 * c), 190 + (190 * l), 100 + (80 * c), fill="blue")] = etat 
        self.__blocs = blocs

    def cassage(self, canvas, id_rect : int):
        """
        Supprime un bloc sur le canvas à partir de son identifiant et le supprime de la liste des blocs
        """
        couleurs = [None, 'red', 'orange']
        if id_rect in self.__blocs :
            self.__blocs[id_rect] -= 1
            etat = self.__blocs[id_rect]
            if etat > 0:
                canvas.itemconfig(id_rect, fill=couleurs[etat])
            else:
                canvas.delete(id_rect)
                del self.__blocs[id_rect]        

        


