#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that prints a port.
    
    #Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the port
    s.bind(('', port))
    
    #Listen for incoming connections
    s.listen(1)
    
    #Accept a connection
    c, addr = s.accept()
    
    #Receive the message and print it
    c.recv(1024)
    
    #Close the connection
    c.close()
    
    #Close the socket
    s.close()

