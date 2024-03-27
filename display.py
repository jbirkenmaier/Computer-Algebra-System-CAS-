import function_library as fl
import tkinter as tk

root = tk.Tk() #create a window
root.title("Input Window")
root.geometry("1000x1000")

def printInput(): 
    inp = inputtxt.get("end-1c linestart", "end-1c lineend")
    label = tk.Label(root, text = inp)
    label.pack()

def on_enter(event):
    printInput()

inputtxt = tk.Text(root, height = 20, width = 150) 
inputtxt.pack()
inputtxt.bind("<Return>",on_enter)


root.mainloop()
