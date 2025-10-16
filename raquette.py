import tkinter as tk

class palet:
    def __init__(self, canvas):
        self.canvas = canvas
        self.palet = canvas.create_rectangle(710, 730, 820, 745, fill="black")
        self.mur_d=820
        self.mur_g=710

    def droite(self,canvas):
        if self.mur_d==canvas.create_rectangle(1810, 730, 1920, 745, fill="black"):
            canvas.delete(self.palet)
        else : 
            canvas.move(self.palet, 10, 0)
            mur_d+=5
            mur_g+=5            


    def gauche(self,canvas):
        if self.mur_d>=0:
            canvas.move(self.palet, 10, 0)
            self.mur_g-=5
            self.mur_d-=5