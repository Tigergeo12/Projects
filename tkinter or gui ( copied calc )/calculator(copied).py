import tkinter as tk #importing library

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation)) #eval() function is used to evaluate the expression
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()  
        text_result.insert(1.0, "Error")
    pass

def clea_field():
    global calculation
    calculation = ""
    


root = tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root , height = 2 , width = 16 , font=("arial" , 24))
text_result.grid(columnspan = 5)
root.mainloop()