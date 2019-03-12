import turtle
import os
import time
import tkinter

global turtles
global turtle
turtles = {}
display = turtle.Screen()

def runCode(code, team):
    try:
        exec(code)
    except:
        print("Error from team "+str(team)+"!")

def reset():
    print("Reset Screen...")
    display.resetscreen()

yurtle = turtle.Turtle()
yurtle.color("white")

while True:
    displaycache = os.listdir("display/")
    time.sleep(.2)
    
    for file in displaycache:
        data = open("display/"+file, "r").read()
        team = int(file)
        runCode(data, team)

        os.remove("display/"+file)
