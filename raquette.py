import tkinter as tk

class palet:
    def __init__(self, canvas):
        self.canvas = canvas
        self.palet = canvas.create_rectangle(710, 930, 820, 945, fill="black")
        self.mur_d=820
        self.mur_g=710

    def droite(self,canvas):
        if self.mur_d <1920:
            canvas.move(self.palet, 10, 0)
            self.mur_d+=10
            self.mur_g+=10            
            print(self.mur_d)

    def gauche(self,canvas):
        if self.mur_g >0:
            canvas.move(self.palet, -10, 0)
            self.mur_g-=10
            self.mur_d-=10
            print(self.mur_g)