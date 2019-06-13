import socket
from tkinter import *

port = 5504





    

class popup(Tk):
    def __init__(self, master = None):
        super().__init__()
        fr =Frame(self)
        lab = Label(fr, text="Enter Host IP:")
        box = Entry(fr)
        ok = Button(fr, text="Ok", command = lambda: self.getip(box.get()))
        fr.pack()
        lab.grid(row = 0, column = 0)
        box.grid(row = 0, column = 1)
        ok.grid(row = 1, column = 1)

    def getip(self, entry):
        global host
        host = entry
        global mySocket
        global Message
        message = "print('Error')"
        mySocket = socket.socket()
        mySocket.connect((host,port))
        self.destroy()

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
    app = popup()
    sender = Window(root)
    #Disabled During Testing as its annoying
    #root.protocol("WM_DELETE_WINDOW", disable_event)
    
    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    #root.after_idle(self.root.call, 'wm', 'attributes', '.', '-topmost', False)
    
    try:
        while True:
            app.update()
            root.update()
    except:
        root.mainloop()
    
if __name__ == '__main__':
    Main()
    

