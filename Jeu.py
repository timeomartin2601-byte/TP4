'''
Class Jeu
Martin Timeo, Braz Arno
19/10/25
TODO : DocString
'''
import tkinter as tk
from time import perf_counter
from PIL import ImageTk

class jeu :
    def __init__(self, fenetre, vies = 1):
        ''' 
        Initialise l'objet jeu
        Entrée : fenetre - tkinter.Frame, fenêtre d'événement tkinter
                 vies - int, nombre de vies du joueur
        '''
        self.__vies = vies
        self.__win = fenetre
        
        self.suppr_autre_win()

        self.__frame_canvas = tk.Frame(fenetre, width=700, height=800)
        self.__frame_canvas.pack(fill='both', expand=True)

        self.__canvas = tk.Canvas(self.__frame_canvas, bg="#302f2f" , width=700, height=800)
        self.__canvas.pack(fill='both')

        self.__canvas.create_line(0, 0, 700, 0, fill="#302f2f" , width=10)
        self.__canvas.create_line(0, 0, 0, 800, fill="#302f2f" , width=10)
        self.__canvas.create_line(700, 0, 700, 800, fill="#302f2f" , width=10)

    def suppr_autre_win(self):
        ''' Détruit les fenêtres existantes à l'exception de la frame info '''
        if len(self.__win.winfo_children()) > 1:
            for frame in self.__win.winfo_children()[1:]:
                frame.destroy()

    def lecanvas(self):
        ''' Renvoie le tkinter Canvas '''
        return self.__canvas
    
    def frame(self):
        ''' Renvoie la tkinter Frame '''
        return self.__frame_canvas
    
    def moins_vie(self):
        ''' Mis à jour du nombre de vies à chaque appel de la fonction '''
        self.__vies -= 1

    def destruction(self):
        ''' Détruit la Tkinter Frame du jeu '''
        self.__frame_canvas.destroy()
