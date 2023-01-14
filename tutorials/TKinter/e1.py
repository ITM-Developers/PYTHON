#Import the tkinter library
import tkinter as tk

def keyup(e):
    print('up', e.char)

def keydown(e):
    print('down', e.char)
    window.destroy()

def on_focus_out(event):
    print('lost focus')

def on_focus_in(event):
    print('get focus')



#Create an instance of tkinter frame
window = tk.Tk()
#Set the geometry
window.geometry("650x250")

#Add a text label and add the font property to it
label= tk.Label(window, text= "Hello World!", font=('Times New Roman bold',20))
label.pack(padx=10, pady=10)

#Create a fullscreen window
#window.attributes('-fullscreen', True)
window.attributes("-topmost", True)

window.bind("<KeyPress>", keydown)
window.bind("<KeyRelease>", keyup)
window.bind("<FocusIn>", on_focus_in)
window.bind("<FocusOut>", on_focus_out)
window.lift()

window.mainloop()