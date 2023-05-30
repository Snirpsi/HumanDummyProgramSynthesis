#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    port = int(sys.argv[1])
    
    # Create a socket and connect to the port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    # Send a message and receive a response
    s.sendall(b'Hello, world!')
    
    # Close the socket
    s.close()
    
    # Close the port
    