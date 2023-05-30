#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    
    port = sys.argv[1]
    
    while True:
        
        # Open a socket to the port and read from it
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((port, 0))
        
        # Read from the socket
        buf = sock.recv(1024)
        
        # Print the received data
        print(buf)
        
        # Close the socket
        sock.close()
        
        # Wait for a keypress to exit
        