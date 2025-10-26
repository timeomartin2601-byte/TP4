'''
Classe Frame d'information
Braz Arno, Martin Timeo
16/10/25
'''
from tkinter import tk

class info:
    def __init__(self, window):
        self.__frame_info = tk.Frame(window, width=700, height=200, bg='grey')

        self.__frame_info.pack(fill='both')

        label_vies=tk.Label(self.__frame_info, text='Nombre de vie : ',fg='white',bg='black')
        label_vies.pack(side='left')

        label_timer=tk.Label(self.__frame_info, text='chrono : ',fg='white',bg='black')
        label_timer.pack(side='left')

        label_score=tk.Label(self.__frame_info, text='score : ',fg='white',bg='black')
        label_score.pack(side='left')

        btn_close = tk.Button(self.__frame_info, text="X", command=window.destroy)
        btn_close.pack(side='right')

        self.__btn_retour = None
        self.__btn_rejouer = None


    def restart(self, fct_retour, fct_rejouer,window):
        self.__btn_retour = tk.Button(window, text='retour menu' , command=fct_retour, fg='white', bg='black').pack(side='left')
        self.__btn_rejouer = tk.Button(window, text='rejouer', command=fct_rejouer,fg='white', bg='black').pack(side='left')

    def nb_bouton(self):
        return len([b for b in self.__frame_info if isinstance(b, tk.Button)])
    
    def detruire(self):
        self.__btn_retour.destroy()
        self.__btn_retour.destroy()