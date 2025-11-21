'''
Class Menu
Martin Timeo, Braz Arno
19/10/25
'''
import tkinter as tk
from tkinter import ttk
from ast import literal_eval

class lemenu :
    def __init__(self, fenetre):
        ''' Initialise l'objet menu '''
        self.__vies = 1
        self.__diff = 1
        self.__win = fenetre
        self.__vies_var = tk.IntVar(value=self.__vies)
        self.__diff_var = tk.IntVar(value=self.__diff)

        self.__meilleurs_scores = [['facile'],['moyen'],['difficile']]
        self.__donnée_str = ''
        self.__donnée_list=''
        
        self.suppr_autre_win()
        self.recup_donnée()

        # Styles de base
        couleur_fond = "#302f2f" 
        couleur_police = '#ffffff'
        police_titre=('Helvetica', 30, 'bold')
        police_sous_titre=('Helvetica', 16, 'bold')
        police_val=('Helvetica', 12, 'bold')

        # Configuration des styles
        style = ttk.Style()
        style.configure('Menu.TFrame', background=couleur_fond)
        style.configure('Titre.TLabel', background = couleur_fond , foreground = couleur_police,font=police_titre)
        style.configure('vies.TLabel',background = couleur_fond , foreground = couleur_police,font=police_sous_titre)
        style.configure('statue_val.TLabel',background = couleur_fond , foreground = couleur_police,font=police_val)
        style.configure('jouer.TButton', font=('Helvetica', 14, 'bold'), padding=10)

        self.__frame_menu = ttk.Frame(fenetre, width=700, height=800, style='Menu.TFrame')
        self.__frame_menu.pack(fill='both', expand=True)

        # Titre
        ttk.Label(self.__frame_menu, text='Jeu du Casse-Brique', style='Titre.TLabel').pack(pady=40)

        # Nombre de vies
        ttk.Label(self.__frame_menu, text='Nombre de vies (1 à 5) :',style='vies.TLabel').pack(pady=10)

        vies_frame = ttk.Frame(self.__frame_menu, style='Menu.TFrame')
        vies_frame.pack(pady=(0, 20))

        self.__vies_slider = ttk.Scale(vies_frame,from_=1,to=5,variable=self.__vies_var,command=self.update_vies_label,length=200)
        self.__vies_slider.pack(side='left', padx=15,pady=5)

        self.__vies_label = ttk.Label(vies_frame, textvariable=self.__vies_var, style='statue_val.TLabel')
        self.__vies_label.pack(side='left')

        # Niveau de difficulté
        ttk.Label(self.__frame_menu, text='Niveau de difficulté (1 à 3) :',style='vies.TLabel').pack(pady=10)

        diff_frame = ttk.Frame(self.__frame_menu, style='Menu.TFrame')
        diff_frame.pack(pady=(0, 20))

        self.__diff_slider = ttk.Scale(diff_frame,from_=1,to=3,variable=self.__diff_var,command=self.update_diff_label,length=200)
        self.__diff_slider.pack(side='left', padx=15,pady=5)

        self.__diff_label = ttk.Label(diff_frame, textvariable=self.__diff_var, style='statue_val.TLabel')
        self.__diff_label.pack(side='left')

        #boutton Jouer
        self.__btn_jouer = ttk.Button(self.__frame_menu, text='Nouvelle Partie', style='jouer.TButton')
        self.__btn_jouer.pack(pady=(30, 0))

        #Dernier record
        stat_frame_titre = ttk.Frame(self.__frame_menu, style='Menu.TFrame')
        stat_frame_titre.pack(pady=(40,0))

        # En-têtes de colonnes
        ttk.Label(stat_frame_titre, text='CLASSEMENT', style='vies.TLabel').pack(pady=20)
        ttk.Label(stat_frame_titre, text='difficulté', style='vies.TLabel').pack(side='left',padx=40)
        ttk.Label(stat_frame_titre, text='Score', style='vies.TLabel').pack(side='left',padx=40)
        ttk.Label(stat_frame_titre, text='Chrono', style='vies.TLabel').pack(side='left',padx=40)

        stat_frame = ttk.Frame(self.__frame_menu, style='Menu.TFrame')
        stat_frame.pack(pady=20, padx=50)

        for i, (difficulté,score, chrono) in enumerate(self.__meilleurs_scores):
            # difficulté (colonne 0)
            ttk.Label(stat_frame, text=f'{difficulté} ({i+1})', style='statue_val.TLabel').grid(row=i + 1, column=0, pady=5, padx=40)
            # Score (colonne 1)
            ttk.Label(stat_frame, text=f'{score}', style='statue_val.TLabel').grid(row=i + 1, column=1, pady=5,padx=(50,50))
            # Chrono (colonne 2)
            ttk.Label(stat_frame, text=f'{round(chrono,2)} s', style='statue_val.TLabel').grid(row=i + 1, column=2, pady=5, padx=40)

    def update_vies_label(self,val):
        ''' Mis à jour du Label vies à chaque appel de la fonction '''
        self.__vies_var.set(int(float(val)))

    def update_diff_label(self,val):
        ''' Mis à jour du Label difficulté à chaque appel de la fonction '''
        self.__diff_var.set(int(float(val)))

    def jouer(self,fct):
        ''' 
        Association au bouton rejouer de la fonction d'entrée
        Entrée : fct - fonction, fonction rejouer à associer au bouton
        '''
        self.__fct_jouer = fct
        if self.__btn_jouer:
            self.__btn_jouer.config(command=self.__fct_jouer)

    def suppr_autre_win(self):
        ''' Détruit les fenêtres existantes à l'exception de la frame info '''
        if len(self.__win.winfo_children()) > 1:
            for frame in self.__win.winfo_children()[1:]:
                frame.destroy()

    def frame(self):
        ''' Renvoie la tkinter Frame du menu '''
        return self.__frame_menu
    
    def difficulte(self):
        ''' Renvoie la difficulté '''
        return self.__diff_var.get()

    def nb_vies(self):
        ''' Renvoie le nombre de vies restantes '''
        return self.__vies_var.get()

    def recup_donnée(self):
        ''' Récupère les données des meilleurs scores '''
        self.__donnée_str = open("data.txt", "r")
        self.__donnée_list=literal_eval("".join(list(self.__donnée_str)))
        for i in range(3):
            self.__meilleurs_scores[i].append(self.__donnée_list[1][i][-1])
            self.__meilleurs_scores[i].append(self.__donnée_list[3][i][0])

    def existe(self):
        '''
        Renvoie si la frame menu existe 
        Sortie : Bool, True si frame_menu existe False sinon
        '''
        return self.__frame_menu.winfo_exists()