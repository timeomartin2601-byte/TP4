import tkinter as tk

class palet:
    def __init__(self, canvas):
        self.canvas = canvas
        self.palet = canvas.create_rectangle(710, 730, 820, 745, fill="black")

<<<<<<< Updated upstream
    def droite(self,canvas):
        canvas.move(self.palet, 5, 0)
=======
class palet : 
    def __init__(self,canvas):
        palet=canvas.create_rectangle(710,630,820,645,  fill="black")
        self.palet=palet

    def droite(canvas) :
        pass


>>>>>>> Stashed changes
