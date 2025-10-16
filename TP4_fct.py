from tkinter import Tk,Label,Canvas,Button

mw=Tk()
mw.title("casse brique")
mw.geometry('1920x1080')


canva=Canvas(mw, bg = 'snow' ) 
canva.grid(row = 0, column = 0, ipadx = 1920, ipady = 1080 )


l = Label(canva,bg = "snow")
l.grid(row = 0, column = 0, ipadx = 100, padx = 0)

l1 = Label(l, text = "Nbr vies : ",bg = "snow")
l1.grid(row = 0, column = 0, ipadx = 20, padx = 0)

l2 = Label(l, text = "score : ",bg = "snow")
l2.grid(row = 0, column = 1, ipadx = 20, padx = 0)

l3 = Label(l,bg = "snow")
l3.grid(row = 0, column = 2, ipadx = 582, padx = 0)



boutton2 = Button( l, text= 'restart', command= mw.destroy, bg = "snow").grid(row = 0, column = 3, ipadx = 20)
boutton1 = Button( l, text= 'quitter', command= mw.destroy, bg = "snow").grid(row = 0, column = 4, ipadx = 20)



for l in range (15) : 
    for c in range (8) : 








mw.mainloop()





