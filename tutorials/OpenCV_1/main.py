from distutils import command
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Sistema de Acceso')
window.geometry("680x480")
window.state('zoomed')

frame = ttk.Frame(window, padding=10)
frame.grid()
ttk.Label(frame, text="Ventana").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=window.destroy).grid(column=1,row=0)

window.mainloop()