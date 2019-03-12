import socket
from _thread import *
import turtle
import threading
import os
import ctypes

global teams
global turtles
teams = {}
turtles = {}

def runCode(code, team, addr):
    try:
        exec(code)
    except:
        print("Error from team "+str(team)+"!")

def display(team, code):
    file = open("display/"+str(team), "w+")
    file.write(code)
    file.close()

def on_new_client(csock, addr):
    print("Connection etablished from: " + str(addr))
    teams[addr] = len(teams) + 1
    
    while True:
        data = csock.recv(8192).decode()
        if not data:
            break

        print("Code from team "+str(teams[addr])+": " + str(data))
             
        data = str(data)

        display(teams[addr], data)
    csock.close()

def Main():
    host = "127.0.0.1"
    port = 5504

    if not os.path.exists("display"):
        print("Setting up display cache!")
        os.makedirs("display")

    ctypes.windll.kernel32.SetConsoleTitleW("liveturtle server")
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)

    print("Ensure all clients connect to "+host+".")
    print("Server listening on port 5504!")

    while True:
        conn, addr = mySocket.accept()
        
        start_new_thread(on_new_client, (conn, addr))
        
    mySocket.close()
     
if __name__ == '__main__':
    Main()
