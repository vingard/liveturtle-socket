import socket
#import tkinter as tk
from tkinter import *
host = "localhost" #This works if client and server are the same machine, it'll need to be changed on the day
port = 5504



global mySocket
global Message
message = "print('Error')"
mySocket = socket.socket()
mySocket.connect((host,port))

def sendCommand():
        message = open('turtleCode.py', 'r').read()
        mySocket.send(message.encode())  
        
def disable_event():
    pass

def InitilizeUI():
        root = Tk()
        root.geometry("100x45")
        frame = Frame(root)
        frame.pack()
        root.title("Client")
        
        #Disabled During Debugging as its annoying
        #root.protocol("WM_DELETE_WINDOW", disable_event)

        #Creating Button
        sendButton = Button(frame, text="Send to Board", width="10", height="2", command=sendCommand)
        sendButton.place(x=50, y=0)
        sendButton.pack()
        
        
        root.mainloop()
        
def Main():
        InitilizeUI()
        
if __name__ == '__main__':
    Main()