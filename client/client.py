import socket
 
def Main():
        host = "127.0.0.1"
        port = 5504
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = input(" -> ")
         
        while message != 'q':
                mySocket.send(message.encode())     
                message = input(" -> ")
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
