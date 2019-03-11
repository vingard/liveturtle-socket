import socket
from _thread import *
import turtle
import threading
global teams
global turtles
teams = {}
turtles = {}

def runCode(code, team, addr):
    try:
        turtle = turtles[addr]
        turtle.color("blue")
        exec(code)
    except:
        print("Error from team "+str(team)+"!")

def on_new_client(csock, addr):
    print("Connection etablished from: " + str(addr))
    teams[addr] = len(teams) + 1
    turtles[addr] = turtle.Turtle()
    
    while True:
        data = csock.recv(8192).decode()
        if not data:
            break

        print("Code from team "+str(teams[addr])+": " + str(data))
             
        data = str(data)    
        runCode(data, teams[addr], addr)
    csock.close()

def Main():
    host = "127.0.0.1"
    port = 5504
    #display = turtle.Screen()
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)

    print("Server listening on port 5504!")

    while True:
        conn, addr = mySocket.accept()
        print(str(addr))
        start_new_thread(on_new_client, (conn, addr))
        
    mySocket.close()
     
if __name__ == '__main__':
    Main()
