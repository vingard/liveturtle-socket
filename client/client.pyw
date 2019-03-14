import socket
from tkinter import *

host = "localhost"
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

        sendButton = Button(self, text="Send to Board", width="15", height="2", command=self.sendCommand)

        sendButton.place(x=0, y=0)
    
    def sendCommand(self):
        message = open('turtleCode.py', 'r').read()
        mySocket.send(message.encode())
    

def disable_event():
        pass
    
def Main():
    root = Tk()
    #root.resizable(False, False)
    
    root.resizable(False, False)
    root.geometry("115x40")
    app = Window(root)
    #Disabled During Testing as its annoying
    #root.protocol("WM_DELETE_WINDOW", disable_event)
    
    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    #root.after_idle(self.root.call, 'wm', 'attributes', '.', '-topmost', False)
    
    root.mainloop()
    
if __name__ == '__main__':
    Main()
    

