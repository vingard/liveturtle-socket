import socket
import tkinter as tk

host = "127.0.0.1"
port = 5504
global mySocket
mySocket = socket.socket()
mySocket.connect((host,port))

def sendCommand():
        
        message = "print('test')"
        mySocket.send(message.encode())  
        commandNotSent = False

        
def InitilizeUI():
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()

        sendButton = tk.Button(frame, text="Send", command=sendCommand)
        sendButton.pack(side=tk.LEFT)
        

        root.mainloop()
        
def Main():
        InitilizeUI()
        
if __name__ == '__main__':
    Main()
