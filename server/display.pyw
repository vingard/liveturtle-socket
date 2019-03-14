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






yurtle = turtle.Turtle()
yurtle.color("white")


    

def Main():
    #initUI()
    
    while True:
        displaycache = os.listdir("display/")
        time.sleep(.2)
        #This while loop is the reason the proigram stalls: The for loop is not executed if the dir is empty, and the .2 second wait causes input lockout
        #until it gets alleviated by a new program. Making the delay longer could help woth this, but i'm not sure about an overall fix :/
        for file in displaycache:
            try:
                print(int(file))
                team = int(file)
            except:
                print(file)
                team = "server"
            with open("display/"+ file, "r") as data: #This connection was never closed, may contribute to buggyness
                code = data.read() 
            os.remove("display/"+file) #Better to remove before executing in case prog is long
            
            runCode(code, team)

            

if __name__ == "__main__":
    Main()
            
        
