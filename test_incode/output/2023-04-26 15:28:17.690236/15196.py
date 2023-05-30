#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input and opens a port. """    
    
    port = int(input("Enter the port number: "))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("", port))
    
    sock.close()
    
