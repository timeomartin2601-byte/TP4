'''
Classe Frame d'information
Braz Arno, Martin Timeo
16/10/25
'''
import tkinter as tk

class info:
    def __init__(self, window):
        ''' 
        Création de la fenêtre d'information et du bouton fermer le programme. 
        Initialise également les différents outils d'information.
        '''
        self.__frame_info = tk.Frame(window, width=700, height=200, bg='grey')

        self.__frame_info.pack(fill='both')

        btn_close = tk.Button(self.__frame_info, text="X", command=window.destroy)
        btn_close.pack(side='right',padx=5)
        btn_close.pack(side='right',padx=(5,0))

        self.__btn_retour = None
        self.__btn_rejouer = None
        self.__label_vies = None
        self.__label_timer = None
        self.__label_score = None

    def restart(self, fct_retour, fct_rejouer):
        '''
        Création des boutons rejouer et retour menu et associations à leurs commandes
        Entrée :    fct_retour - fonction, Affiche le menu principal au joueur
                    fct_rejouer - fonction, Relance la page de jeu aux valeurs par défaut
        '''
        self.__label_vies=tk.Label(self.__frame_info, text='Nombre de vie : ',fg='white',bg='grey')
        self.__label_vies.pack(side='left',padx=5)

        self.__label_timer=tk.Label(self.__frame_info, text='chrono : ',fg='white',bg='grey')
        self.__label_timer.pack(side='left',padx=5)

        self.__label_score=tk.Label(self.__frame_info, text='score : ',fg='white',bg='grey')
        self.__label_score.pack(side='left',padx=5)

        self.__btn_retour = tk.Button(self.__frame_info, text='retour menu' , command=fct_retour)
        self.__btn_retour.pack(side='right',padx=5)
        self.__btn_rejouer = tk.Button(self.__frame_info, text='rejouer', command=fct_rejouer)
        self.__btn_rejouer.pack(side='right',padx=5)
    
    def detruire(self):
        '''
        Détruit les labels et boutons à l'appel de la fonction
        '''
        self.__label_vies.destroy()
        self.__label_timer.destroy()
        self.__label_score.destroy()
        self.__btn_retour.destroy()
        self.__btn_rejouer.destroy()

    def btn_presents(self):
        '''
        Retourne si les boutons rejouer et retour menu sont présents dans la frame
        Sortie : Bool, True si les boutons ne sont pas présents, False sinon
        '''
        return self.__btn_retour is not None and self.__btn_rejouer is not None
    
    def update_labels(self, vies, chrono, score):
        '''
        La fonction met à jour les labels à chaque appel
        '''
        self.__label_vies.config(text='Nombre de vie : ' + str(vies))
        self.__label_timer.config(text='chrono : ' + str(round(chrono, 2)) + 's')
        self.__label_score.config(text='score : ' + str(score))
