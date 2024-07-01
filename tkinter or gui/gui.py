import tkinter as tk #importing library

window = tk.Tk() #creating a window

window.geometry("500x700")
window.title("calculator")

label = tk.Label(window , text = "hello" , font = ("Arial" , 20))
label.pack(padx = 40 , pady = 10) #packing the label in the window

window.mainloop() # running the window
