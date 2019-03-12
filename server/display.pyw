import turtle
import os
import time
from tkinter import *
from _thread import *

display = turtle.Screen()
yurtle = turtle.Turtle()
yurtle.color("white")

def runCode(code, team):
    try:
        exec(code)
    except:
        print("Error from team "+str(team)+"!")

def reset():
    print("Reset Screen...")
    display.resetscreen()
    turtle.color("white")
 

def refresh():
    displaycache = os.listdir("display/")
    time.sleep(.2)
    for file in displaycache:
        print(int(file))
        with open("display/"+ file, "r") as data: #This connection was never closed, may contribute to buggyness
            code = data.read() 
        os.remove("display/"+file) #Better to remove before executing in case prog is long
        team = int(file)
        runCode(code, team)

def Main():
    root = Tk()
    root.geometry("100x100")
    frame = Frame(root)
    frame.pack()
    root.title("Display")
    resetButton = Button(frame, text="Reset", width="10", height="2", command=reset)
    resetButton.place(x=50, y=0)
    resetButton.pack()
    refreshButton = Button(frame, text="Refresh", width="10", height="2", command=refresh)
    refreshButton.place(x=50, y=50)
    refreshButton.pack()
    refresh()

            

if __name__ == "__main__":
    Main()
            
        
