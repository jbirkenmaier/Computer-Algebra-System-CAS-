import function_library as fl
import tkinter as tk


root = tk.Tk() #create a window
input_counter = 0
root.title("Input Window")
root.geometry("1000x1000")

def printInput(): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)
    label.pack()
    read_input(inp)
    
def read_input(inp):
    global input_counter  # Declare input_counter as global
    line_object = fl.classify_line(inp,input_counter)
    input_counter+=1
    line_object.calculate()
    print(input_counter, line_object.result)
    result_label = tk.Label(root, text = str(line_object.result))
    #currently the result object and calculate function only exists in the Calc_object class
    result_label.pack()


def on_enter(event):
    printInput()

inputtxt = tk.Text(root, height = 20, width = 150) 
inputtxt.pack()
inputtxt.bind("<Return>",on_enter)


root.mainloop()
