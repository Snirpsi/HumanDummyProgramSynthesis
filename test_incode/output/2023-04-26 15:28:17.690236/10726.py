#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input and returns a port. """    
    port = int(input("Enter a port number: "))
    
    print("Opening port " + str(port))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    sock.close()
    
    print("Port closed")
    
    
