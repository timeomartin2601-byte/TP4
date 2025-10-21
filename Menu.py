'''
Class Menu
Martin Timeo, Braz Arno
19/10/25
TODO Faire en sorte de pouvoir être rouvert
'''
import tkinter as tk

class menu :
    def __init__(self, fenetre, vies = 3, difficulte = 1):
        self.__vies = vies
        self.__diff = difficulte
        self.__win = fenetre

        frame_menu = tk.Frame(fenetre, width=700, height=800)
        frame_menu.pack(fill='both', expand=True)

        tk.Label(frame_menu, text='Jeu du Casse-Brique !', height=5).pack()

        tk.Label(frame_menu, text='Nombre de vie (3 par défaut) :').pack()
        vies_entry = tk.Entry(frame_menu)
        vies_entry.pack()

        tk.Label(frame_menu, text='difficulté (1 à 3) :').pack()
        diff_entry = tk.Entry(frame_menu)
        diff_entry.pack()

        if entier(vies_entry.get()):
            self.__vies = int(vies_entry.get())
    
        if diff_entry.get() in ['1', '2', '3']: 
            self.__diff = int(diff_entry.get())

    def sup_autre_win(self):
        if len(self.__win.winfo_children()) > 1:
            for frame in self.__win.winfo_children()[1:]:
                frame.destroy()

    def entier(self, valeur):
        if valeur != '':
            for elt in valeur :
                if elt not in '0123456789':
                    return False
            return True
        else:
            return False