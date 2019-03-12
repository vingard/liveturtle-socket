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


#def initUI(): This all doesn't really work, some take a look while i do my exam lol
#    root = Tk()
#    root.geometry("100x45")
#    frame = Frame(root)
#    frame.pack()
#    root.title("Display")
#    resetButton = Button(frame, text="Reset", width="10", height="2", command=reset)
#    resetButton.place(x=50, y=0)
#    resetButton.pack()

yurtle = turtle.Turtle()
yurtle.color("white")


    

def Main():
    initUI()
    while True:
        displaycache = os.listdir("display/")
        time.sleep(.2)
        #This while loop is the reason the proigram stalls: The for loop is not executed if the dir is empty, and the .2 second wait causes input lockout
        #until it gets alleviated by a new program. Making the delay longer could help woth this, but i'm not sure about an overall fix :/
        for file in displaycache:
            print(int(file))
            with open("display/"+ file, "r") as data: #This connection was never closed, may contribute to buggyness
                code = data.read() 
            os.remove("display/"+file) #Better to remove before executing in case prog is long
            team = int(file)
            runCode(code, team)

            

if __name__ == "__main__":
    Main()
            
        
