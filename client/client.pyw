import socket
from tkinter import *

host = "127.0.0.1"
port = 5504

global mySocket
global Message
message = "print('Error')"
mySocket = socket.socket()
mySocket.connect((host,port))

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()
    
    
    def init_window(self):
        self.master.title("Client")
        self.pack(fill = BOTH, expand = 1)

        sendButton = Button(self, text="Send", width="10", height="2", command=self.sendCommand)

        sendButton.place(x =50, y = 0)
    
    def sendCommand(self):
        message = open('turtleCode.py', 'r').read()
        mySocket.send(message.encode())
    

def disable_event():
        pass
    
def Main():
    root = Tk()
    root.geometry("500x500")
    app = Window(root)
    #Disabled During Testing as its annoying
    #root.protocol("WM_DELETE_WINDOW", disable_event)
    root.mainloop()
    
if __name__ == '__main__':
    Main()
    

