'''
Class Blocs
Martin Timeo, Braz Arno
09/10/25
todo : detection de collision ici ?
'''
import tkinter as tk

class Blocs:
    def __init__(self, canvas): #, blocs: dict):
        """
        blocs : dictionnaire {coord: id_rectangle}
        """
        blocs = dict()
        for l in range(10):
            for c in range(5):
                blocs[(10 + (190 * l), 30 + (80 * c))] = canvas.create_rectangle(10 + (190 * l), 30 + (80 * c),
                                                                                190 + (190 * l), 100 + (80 * c),
                                                                                fill="blue")
        self.__blocs = blocs

    def cassage(self, canvas, coord : tuple):
        """
        Supprime un bloc sur le canvas à partir de ses coordonnées-clé
        """
        if coord in self._blocs:
            canvas.delete(self.__blocs[coord])
            del self.__blocs[coord]  # Optionnel : on le retire du dict

        


