import tkinter as tk

class palet:
    def __init__(self, canvas):
        self.canvas = canvas
        self.palet = canvas.create_rectangle(710, 730, 820, 745, fill="black")

    def droite(self,canvas):
        canvas.move(self.palet, 10, 0)        


    def gauche(self,canvas):
        canvas.move(self.palet, -10, 0)