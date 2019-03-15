import socket
from _thread import *
import threading
import os
import ctypes
from tkinter import *
global teams
teams = {}

def display(team, code):
    with open("display/"+str(team), "w+") as file: #Cleaner solution to file handling
       file.write(code)

def reset():
    with open('display/reset','w+') as reset:
        reset.write("""display.resetscreen()\nturtle.color("white")""")
    print("Reset Screen...")
    

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

def initUI(): 
    root = Tk()
    root.geometry("100x45")
    frame = Frame(root)
    frame.pack()
    root.title("Display")
    resetButton = Button(frame, text="Reset", width="10", height="2", command=reset)
    resetButton.place(x=50, y=0)
    resetButton.pack()
    return root

def conmanager(sSocket):
    while True:
        conn, addr = sSocket.accept() 
        start_new_thread(on_new_client, (conn, addr))


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

    if host == "localhost" or host == "127.0.0.1":
        print("You are running the server on localhost! This should only be used in development.")
        print("THIS MEANS CLIENTS OTHER THAN YOUR COMPUTER CANNOT CONNECT.")
        print("To run the server properly, set the host to your local IPv4 address.")

    tkroot = initUI()
    start_new_thread(conmanager,(mySocket,))
    tkroot.mainloop()
    
        

    mySocket.close()
     
if __name__ == '__main__':
    Main()
