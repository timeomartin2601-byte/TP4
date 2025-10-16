import tkinter as tk

mw=tk.Tk()
mw.title("casse brique")
mw.geometry('1920x1080')


canvas=tk.Canvas(mw, bg = 'ivory' ) 
canvas.grid(row = 0, column = 0, ipadx = 1920, ipady = 1080 )



l = tk.Label(canvas, text = "Nbr vies : ",bg = "red")
l.grid(row = 0, column = 0, ipadx = 100, padx = 0)

l2 = tk.Label(canvas, text = "Nbr vies : ",bg = "red")
l2.grid(row = 0, column = 1, ipadx = 100, padx = 1020)


for l in range(15):
    for c in range(8):
        canvas.create_rectangle(20+(100*l), 30+(40*c), 110+(100*l), 60+(40*c), fill= "blue")


tk.mainloop()