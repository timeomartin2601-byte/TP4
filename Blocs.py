'''
Class Blocs
Martin Timeo, Braz Arno
09/10/25
todo : affichage dans fichier principal
'''
import tkinter as tk

class Blocs:
    def __init__(self, canvas): #, blocs: dict):
        """
        blocs : dictionnaire {coord: id_rectangle}
        """
        blocs = dict()
        for l in range(15):
            for c in range(8):
                blocs[(20 + (100 * l), 30 + (40 * c))] = canvas.create_rectangle(20 + (100 * l), 30 + (40 * c),
                                                                                110 + (100 * l), 60 + (40 * c),
                                                                                fill="blue")
        self.__blocs = blocs

    def cassage(self, canvas, coord : tuple):
        """
        Supprime un bloc sur le canvas à partir de ses coordonnées-clé
        """
        if coord in self._blocs:
            canvas.delete(self.__blocs[coord])
            del self.__blocs[coord]  # Optionnel : on le retire du dict

        


