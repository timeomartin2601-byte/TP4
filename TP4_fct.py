from tkinter import Tk,Label,Canvas,Button

mw=Tk()
mw.title("casse brique")
mw.geometry('1920x1080')


canva=Canvas(mw, bg = 'ivory' ) 
canva.grid(row = 0, column = 0, ipadx = 1920, ipady = 1080 )


l = Label(canva,bg = "red")
l.grid(row = 0, column = 0, ipadx = 100, padx = 0)

l1 = Label(l, text = "Nbr vies : ",bg = "green")
l1.grid(row = 0, column = 0, ipadx = 100, padx = 0)

l2 = Label(l, text = "score : ",bg = "green")
l2.grid(row = 0, column = 1, ipadx = 100, padx = 0)

boutton = Button( l, text= 'quitter', command= mw.destroy)
boutton.grid(row = 0, column = 2, ipadx = 100, padx = 200)

for l in range (15) : 
    for c in range (8) : 
        canva.create_rectangle(20 + ( 100 * l ), 30 + ( 40 * c ), 110 + ( 100 * l ) , 60 + ( 40 * c ), fill="blue")



mw.mainloop()