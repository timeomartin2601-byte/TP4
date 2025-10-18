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
        blocs : list, l'entièreté des identifiants des blocs
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
        Supprime un bloc sur le canvas à partir de son identifiant et le supprime de la liste des blocs
        """
        if id_rect in self.__blocs :
            canvas.delete(id_rect)
            self.__blocs.remove(id_rect)

        


