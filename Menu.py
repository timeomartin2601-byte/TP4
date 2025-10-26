'''
Class Menu
Martin Timeo, Braz Arno
19/10/25
TODO Faire en sorte de pouvoir être rouvert
'''
import tkinter as tk
from tkinter import ttk

class lemenu :
    def __init__(self, fenetre):
        self.__vies = 3
        self.__diff = 1
        self.__win = fenetre
        self.__vies_var = tk.IntVar(value=self.__vies)
        self.__diff_var = tk.IntVar(value=self.__diff)
        
        self.suppr_autre_win()

        # Styles de base
        couleur_fond = "#302f2f" 
        couleur_police = '#ffffff'
        police_titre=('Helvetica', 20, 'bold')
        police_sous_titre=('Helvetica', 15, 'bold')
        police_val=('Helvetica', 10, 'bold')

        # Configuration des styles
        style = ttk.Style()
        style.configure('Menu.TFrame', background=couleur_fond)
        style.configure('Titre.TLabel', background = couleur_fond , foreground = couleur_police,font=police_titre)
        style.configure('vies.TLabel',background = couleur_fond , foreground = couleur_police,font=police_sous_titre)
        style.configure('statue_val.TLabel',background = couleur_fond , foreground = couleur_police,font=police_val)
        style.configure('Jouer.TButton',background = couleur_fond , foreground = couleur_police , font=police_sous_titre)

        self.__frame_menu = ttk.Frame(fenetre, width=700, height=800, style='Menu.TFrame')
        self.__frame_menu.pack(fill='both', expand=True)

        # Titre
        ttk.Label(self.__frame_menu, text='Jeu du Casse-Brique !', style='Titre.TLabel').pack(pady=(40, 20))



        # Nombre de vies
        ttk.Label(self.__frame_menu, text='Nombre de vies (1 à 5) :',style='vies.TLabel').pack(pady=(10, 5))

        vies_frame = ttk.Frame(self.__frame_menu, style='Menu.TFrame')
        vies_frame.pack(pady=(0, 20))

        self.__vies_slider = ttk.Scale(vies_frame,from_=1,to=5,variable=self.__vies_var,command=self.update_vies_label,length=200)
        self.__vies_slider.pack(side='left', padx=10)

        self.__vies_label = ttk.Label(vies_frame, textvariable=self.__vies_var, style='statue_val.TLabel')
        self.__vies_label.pack(side='left')


        # Niveau de difficulté
        ttk.Label(self.__frame_menu, text='Niveau de difficulté (1 à 3) :',style='vies.TLabel').pack(pady=(10, 5))

        diff_frame = ttk.Frame(self.__frame_menu, style='Menu.TFrame')
        diff_frame.pack(pady=(0, 20))

        self.__diff_slider = ttk.Scale(diff_frame,from_=1,to=3,variable=self.__diff_var,command=self.update_diff_label,length=200)
        self.__diff_slider.pack(side='left', padx=10)

        self.__diff_label = ttk.Label(diff_frame, textvariable=self.__diff_var, style='statue_val.TLabel')
        self.__diff_label.pack(side='left')

        #boutton Jouer
        self.__btn_jouer = ttk.Button(self.__frame_menu, text='Nouvelle Partie', style='jouer.TButton')
        self.__btn_jouer.pack(pady=(30, 0))


    def update_vies_label(self,val):
        self.__vies_var.set(int(float(val)))

    def update_diff_label(self,val):
        self.__diff_var.set(int(float(val)))

    def jouer(self,fct):
        self.__fct_jouer = fct
        if self.__btn_jouer:
            self.__btn_jouer.config(command=self.__fct_jouer)

    def suppr_autre_win(self):
        if len(self.__win.winfo_children()) > 1:
            for frame in self.__win.winfo_children()[1:]:
                frame.destroy()

    def frame(self):
        return self.__frame_menu
    
    def difficulte(self):
        return self.__diff_var.get()

    def nb_vies(self):
        return self.__vies_var.get()

