'''
Class Jeu
Martin Timeo, Braz Arno
19/10/25
'''
from tkinter import ttk
from ast import literal_eval

class lemenu_fin:
    def __init__(self,fenetre,difficulté):

        #recuperation de l'historique des scores/chrono et des meilleurs scores/chrono
        self.__meilleurs_perf = [[],[],[]]
        self.__historique_perf = [[],[],[]]
        self.recup_donnée(difficulté)


        # Styles de base
        couleur_fond = "#302f2f" 
        couleur_du_titre ="#c91616"
        couleur_police = "#ffffff"
        police_titre=('Helvetica', 30, 'bold')
        police_sous_titre=('Helvetica', 15, 'bold')
        police_val=('Helvetica', 12, 'bold')


        # Configuration des styles
        style = ttk.Style()
        style.configure('Menu.TFrame',background = couleur_fond)
        style.configure('Titre.TLabel', background = couleur_fond , foreground = couleur_du_titre,font=police_titre)
        style.configure('sous_titre.TLabel',background = couleur_fond , foreground = couleur_police,font=police_sous_titre)
        style.configure('statue_val.TLabel',background = couleur_fond , foreground = couleur_police,font=police_val)
        style.configure('jouer.TButton',background = couleur_fond, font=('Helvetica', 14, 'bold'), padding=10)


        #Initialisation Frame Principale du Menu de fin
        self.__Frame_fin=ttk.Frame(fenetre,width=700,height=800,style='Menu.TFrame')
        self.__Frame_fin.pack(fill='both', expand=True)

        #Titre 
        self.__Label_titre=ttk.Label(self.__Frame_fin,style='Titre.TLabel')
        self.__Label_titre.pack(pady=40)

        #Annonce score
        self.__Frame_score=ttk.Frame(self.__Frame_fin,style='Menu.TFrame')
        self.__Frame_score.pack()

        self.__Label_Score=ttk.Label(self.__Frame_score,text= 'Score: ',style='sous_titre.TLabel')
        self.__Label_Score.pack(side='left', padx=5)

        self.__Label_Score_valeur=ttk.Label(self.__Frame_score,style='sous_titre.TLabel')
        self.__Label_Score_valeur.pack(side='left')


        #Annonce Chrono
        self.__Frame_chrono=ttk.Frame(self.__Frame_fin,style='Menu.TFrame')
        self.__Frame_chrono.pack()
        
        self.__Label_Chrono=ttk.Label(self.__Frame_chrono,text= 'Chrono: ',style='sous_titre.TLabel')
        self.__Label_Chrono.pack(side='left', padx=5)

        self.__Label_Chrono_valeur=ttk.Label(self.__Frame_chrono,style='sous_titre.TLabel')
        self.__Label_Chrono_valeur.pack(side='left')


        #Meilleurs scores et chrono
        self.__stat_frame_record = ttk.Frame(self.__Frame_fin, style='Menu.TFrame')
        self.__stat_frame_record.pack(pady=(20,0))

        # En-tête principal
        ttk.Label(self.__stat_frame_record, text='Meilleurs Records', style='vies.TLabel').grid(row=0, column=0, columnspan=3, pady=20)
        
        # En-têtes de colonnes
        ttk.Label(self.__stat_frame_record, text='Position', style='vies.TLabel').grid(row=1, column=0, padx=40)
        ttk.Label(self.__stat_frame_record, text='Score', style='vies.TLabel').grid(row=1, column=1, padx=40)
        ttk.Label(self.__stat_frame_record, text='Chrono', style='vies.TLabel').grid(row=1, column=2, padx=40)

        for i, (score, chrono) in enumerate(self.__meilleurs_perf):
            # rang (colonne 0)
            ttk.Label(self.__stat_frame_record, text=f'{i+1}', style='statue_val.TLabel').grid(row=i + 2, column=0, pady=5,padx=55)
            # Score (colonne 1)
            ttk.Label(self.__stat_frame_record, text=f'{score}', style='statue_val.TLabel').grid(row=i + 2, column=1, pady=5,padx=55)
            # Chrono (colonne 2)
            ttk.Label(self.__stat_frame_record, text=f'{round(chrono,2)} s', style='statue_val.TLabel').grid(row=i + 2, column=2, pady=5, padx=55)



        #Historique
        self.__stat_frame_historique = ttk.Frame(self.__Frame_fin, style='Menu.TFrame')
        self.__stat_frame_historique.pack(pady=(20,0))

        # En-tête principal
        ttk.Label(self.__stat_frame_historique, text='Historique des Parties', style='vies.TLabel').grid(row=0, column=0, columnspan=3, pady=20)
        
        # En-têtes de colonnes
        ttk.Label(self.__stat_frame_historique, text='Position', style='vies.TLabel').grid(row=1, column=0, padx=40)
        ttk.Label(self.__stat_frame_historique, text='Score', style='vies.TLabel').grid(row=1, column=1, padx=40)
        ttk.Label(self.__stat_frame_historique, text='Chrono', style='vies.TLabel').grid(row=1, column=2, padx=40)
        
        for i, (score, chrono) in enumerate(self.__historique_perf):
            # rang (colonne 0)
            ttk.Label(self.__stat_frame_historique, text=f'{i+1}', style='statue_val.TLabel').grid(row=i + 2, column=0, pady=5,padx=55)
            # Score (colonne 1)
            ttk.Label(self.__stat_frame_historique, text=f'{score}', style='statue_val.TLabel').grid(row=i + 2, column=1, pady=5,padx=55)
            # Chrono (colonne 2)
            ttk.Label(self.__stat_frame_historique, text=f'{round(chrono,2)} s', style='statue_val.TLabel').grid(row=i + 2, column=2, pady=5, padx=55)


    def restart(self,fct_retour,fct_rejouer):
        '''
        Creer une Frame contenant les boutons et affiche les bouton rejouer et retour au menu principale
        parametre : -fct_retour : devient la commande du bouton retour au menu principale
                    -fct_rejouer : devient la commande du bouton rejouer
        '''
        self.__Frame_bouton=ttk.Frame(self.__Frame_fin,style='Menu.TFrame')
        self.__Frame_bouton.pack(pady=20)
        ttk.Button(self.__Frame_bouton,text='retour menu' ,command=fct_retour,style='jouer.TButton').grid(row=0,column=0,padx=10)
        ttk.Button(self.__Frame_bouton,text='rejouer' ,command=fct_rejouer,style='jouer.TButton').grid(row=0,column=1,padx=10)


    def text_titre(self,titre='ERREUR'):
        '''
        modifie le texte du label titre self.__Label_titre
        parametre titre : type str
        '''
        self.__Label_titre.config(text=f'{titre}')

    def nbr_score(self,score=-1):
        '''
        modifie le texte du label self.__Label_Score_valeur
        parametre titre : float
        '''
        self.__Label_Score_valeur.config(text=f'{score}')

    def nbr_chrono(self,chrono=-1):
        '''
        modifie le texte du label self.__Label_Chrono_valeur
        parametre chrono : float positif
        '''
        self.__Label_Chrono_valeur.config(text=f'{chrono}')

    def recup_donnée(self,difficulté):
        '''
        recupere les données du fichier text data.txt qui contient une liste comprenant 4 sous liste.
        corespondance : - 1er sous liste : historique des scores
                        - 2eme sous liste : meilleurs scores
                        - 3eme sous liste : historique des chronos
                        - 4eme sous liste : meilleurs chronos
        Chaque sous liste contient 3 sous liste car 3 difficulté.
        parametre diificulté : entier compris entre 1 et 3
        '''
        self.__donnée_str = open("data.txt", "r")
        self.__donnée_list=literal_eval("".join(list(self.__donnée_str)))
        for i in range(3):
            self.__meilleurs_perf[i].append(self.__donnée_list[1][difficulté-1][-1-i])
            self.__meilleurs_perf[i].append(self.__donnée_list[3][difficulté-1][i])

            self.__historique_perf[i].append(self.__donnée_list[0][difficulté-1][-1-i])
            self.__historique_perf[i].append(self.__donnée_list[2][difficulté-1][i])

