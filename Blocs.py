'''
Class Blocs
Martin Timeo, Braz Arno
09/10/25
todo : detection de collision ici -> non
'''
import tkinter as tk

class Blocs:
    def __init__(self, canvas): #, blocs: dict):
        """
        blocs : dictionnaire {coord: id_rectangle} -> inutile enft 
        """
        # blocs = dict()
        blocs = list()
        for l in range(10):
            for c in range(5):
                # blocs[(10 + (190 * l), 30 + (80 * c))] = canvas.create_rectangle(10 + (190 * l), 30 + (80 * c),
                #                                                                 190 + (190 * l), 100 + (80 * c),
                #                                                                 fill="blue")
                #blocs[canvas.create_rectangle(10 + (190 * l), 30 + (80 * c), 190 + (190 * l), 100 + (80 * c), fill="blue")] = (10 + (190 * l), 30 + (80 * c)) 
                blocs.append(canvas.create_rectangle(10 + (190 * l), 30 + (80 * c), 190 + (190 * l), 100 + (80 * c), fill="blue"))
        self.__blocs = blocs
        # print(self.__blocs) 

    def cassage(self, canvas, id_rect : int):
        """
        Supprime un bloc sur le canvas à partir de ses coordonnées-clé -> justement on va se servir de l'inverse
        """
        # for clef, valeur in self.__blocs.items():
        #     if valeur == id_rect:
        #         canvas.delete(self.__blocs[clef])
        #         del self.__blocs[clef]  
        canvas.delete(id_rect)

        


