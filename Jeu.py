'''
Class Jeu
Martin Timeo, Braz Arno
19/10/25
TODO Faire en sorte de pouvoir être rouvert + importer score ou timer 
'''
import tkinter as tk

class jeu :
    def __init__(self, fenetre, vies = 3):
        self.__vies = vies
        self.__win = fenetre
        
        self.suppr_autre_win()

        self.__frame_canvas = tk.Frame(fenetre, width=700, height=800)
        self.__frame_canvas.pack(fill='both', expand=True)

        self.__canvas = tk.Canvas(self.__frame_canvas, bg='light grey', width=700, height=800)
        self.__canvas.pack(fill='both')

        self.__canvas_fin=tk.Canvas(self.__canvas)

        self.__canvas.create_line(0, 0, 700, 0, fill='green', width=10)
        self.__canvas.create_line(0, 0, 0, 800, fill='green', width=10)
        self.__canvas.create_line(700, 0, 700, 800, fill='green', width=10)

    def suppr_autre_win(self):
        if len(self.__win.winfo_children()) > 1:
            for frame in self.__win.winfo_children()[1:]:
                frame.destroy()

    def lecanvas(self):
        return self.__canvas
    
    def frame(self):
        return self.__frame_canvas
    
    def moins_vie(self):
        self.__vies -= 1
    
    def destruction(self):
        self.__frame_canvas.destroy()

    def restart(self,fct_retour,fct_rejouer,window):
        self.__canvas_fin.place(x=400,y=400)
        btn_retour = tk.Button(self.__canvas_fin,text='retour menu' ,command=fct_retour).pack()
        btn_rejouer = tk.Button(self.__canvas_fin,text='rejouer' ,command=fct_rejouer).pack()




