'''
Class Blocs
Martin Timeo, Braz Arno
09/10/25
TODO : Gerer l'état des blocs (pour + de difficulté)
'''
import tkinter as tk

class Blocs:
    def __init__(self, canvas): 
        """
        blocs : list, l'entièreté des identifiants des blocs 
        TODO revenir sur un dict avec pour val l'état ?  ex. id_bloc : etat
        """
        blocs = dict()
        # blocs = list()
        for l in range(10):
            for c in range(5):
                blocs[canvas.create_rectangle(10 + (190 * l), 30 + (80 * c), 190 + (190 * l), 100 + (80 * c), fill="blue")] = 3 
                # TODO Avec dict on pourrait mettre en val l'état
                # blocs.append(canvas.create_rectangle(10 + (190 * l), 30 + (80 * c), 190 + (190 * l), 100 + (80 * c), fill="blue"))
        self.__blocs = blocs

    def cassage(self, canvas, id_rect : int):
        """
        Supprime un bloc sur le canvas à partir de son identifiant et le supprime de la liste des blocs 
        TODO si etat == 2 : chgt couleur en orange, si etat == 1 : chgt couleur en rouge, si etat == 0 : destruction du bloc
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
        # self.__blocs.remove(id_rect)  # Version avec list

        


