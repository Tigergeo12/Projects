import tkinter as tk #importing library

window = tk.Tk() #creating a window

window.geometry("500x700")
window.title("calculator")

label = tk.Label(window , text = "hello world" , font = ("Arial" , 20))
label.pack(padx = 20 , pady = 20) #packing the label in the window

textbox = tk.Text(window , font = ("arial" , 16) , height = 5) #textbox that the user can write on
textbox.pack()



window.mainloop() # running the window


