from tkinter import Tk,Label,Canvas

mw=Tk()
mw.title("casse brique")
mw.geometry('1920x1080')


canva=Canvas(mw, bg = 'ivory' ) 
canva.grid(row = 0, column = 0, ipadx = 1920, ipady = 1080 )



l = Label(canva, text = "Nbr vies : ",bg = "red")
l.grid(row = 0, column = 0, ipadx = 100, padx = 0)

l2 = Label(canva, text = "Nbr vies : ",bg = "red")
l2.grid(row = 0, column = 1, ipadx = 100, padx = 1020)




mw.mainloop()