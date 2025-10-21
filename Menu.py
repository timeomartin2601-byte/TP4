'''
Class Menu
Martin Timeo, Braz Arno
19/10/25
TODO Faire en sorte de pouvoir être rouvert
'''
import tkinter as tk

class menu :
    def __init__(self, fenetre):
        self.__vies = 3
        self.__diff = 1
        self.__win = fenetre

        self.suppr_autre_win()

        self.__frame_menu = tk.Frame(fenetre, width=700, height=800)
        self.__frame_menu.pack(fill='both', expand=True)

        tk.Label(self.__frame_menu, text='Jeu du Casse-Brique !', height=5).pack()

        tk.Label(self.__frame_menu, text='Nombre de vie (3 par défaut) :').pack()
        vies_entry = tk.Entry(self.__frame_menu)
        vies_entry.pack()

        tk.Label(self.__frame_menu, text='difficulté (1 à 3) :').pack()
        diff_entry = tk.Entry(self.__frame_menu)
        diff_entry.pack()

        if entier(vies_entry.get()):
            self.__vies = int(vies_entry.get())
    
        if diff_entry.get() in ['1', '2', '3']: 
            self.__diff = int(diff_entry.get())

    def suppr_autre_win(self):
        if len(self.__win.winfo_children()) > 1:
            for frame in self.__win.winfo_children()[1:]:
                frame.destroy()

    def frame(self):
        return self.__frame_menu

    def nb_vies(self):
        return self.__vies
    
    def difficulte(self):
        return self.__diff

def entier(valeur):
    if valeur != '':
        for elt in valeur :
            if elt not in '0123456789':
                return False
        return True
    else:
        return False