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
                blocs[(20 + (100 * l), 30 + (40 * c))] = canvas.create_rectangle(
                    20 + (100 * l), 30 + (40 * c),
                    110 + (100 * l), 60 + (40 * c),
                    fill="blue")
        self._blocs = blocs  # Dictionnaire des blocs (coord -> id)

    def cassage(self, canvas, coord=(220, 30)):
        """
        Supprime un bloc sur le canvas à partir de ses coordonnées-clé
        """
        if coord in self._blocs:
            canvas.delete(self._blocs[coord])
            del self._blocs[coord]  # Optionnel : on le retire du dict




