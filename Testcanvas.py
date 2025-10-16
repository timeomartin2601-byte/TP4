import tkinter as tk
import Blocs as blc

mw=tk.Tk()
mw.title("casse brique")
mw.geometry('1920x1080')



canvas=tk.Canvas(mw, bg = 'ivory' ) 
canvas.grid(row = 0, column = 0, ipadx = 1920, ipady = 1080 )

tk.Button(canvas, text="Quitter", command=mw.destroy).grid(row = 0, column = 2, ipadx = 100, padx = 750)

l = tk.Label(canvas, text = "Nbr vies : ",bg = "red")
l.grid(row = 0, column = 0, ipadx = 100, padx = 0)

l2 = tk.Label(canvas, text = "Nbr vies : ",bg = "red")
l2.grid(row = 0, column = 1, ipadx = 100, padx = 10)

blocs = dict()
for l in range(15):
    for c in range(8):
        blocs[(20+(100*l), 30+(40*c))] = canvas.create_rectangle(20+(100*l), 30+(40*c), 110+(100*l), 60+(40*c), fill= "blue")

def on_key(event):
    if event.keysym == "space" :    
        blc.cassage(canvas, blocs)
        canvas.move(blocs[(120, 30)], 300, 300)
        canvas.delete(blocs[(220, 30)])

def destr(event):
    rect = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    print(rect)
    for rectangle in rect :
        canvas.delete(rectangle)



mw.bind("<Key>", on_key)
mw.bind("<Button-1>", destr)
tk.mainloop()