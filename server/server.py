import socket
from _thread import *
import threading
import os
import ctypes

global teams
teams = {}


def display(team, code):
    with open("display/"+str(team), "w+") as file: #Cleaner solution to file handling
       file.write(code)
   

def on_new_client(csock, addr):
    teams[addr] = len(teams) + 1
    print("Connection etablished from [%s] as team %s." % (str(addr), str(teams[addr]))) #Added more info to connection string
    
    while True:
        data = csock.recv(8192).decode()
        if not data:
            break

        data = str(data)
        print("Code from team "+str(teams[addr])+": " + data)
             
    
        display(teams[addr], data)
    csock.close()

def Main():
    host = "localhost"
    port = 5504

    if not os.path.exists("display"):
        print("Setting up display cache!")
        os.makedirs("display")

    ctypes.windll.kernel32.SetConsoleTitleW("liveturtle server on "+host)
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
