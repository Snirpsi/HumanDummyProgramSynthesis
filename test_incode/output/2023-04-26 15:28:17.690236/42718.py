#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports. """    
    
    # Iterate over all ports
    for port in ports:
        
        # Open a socket to the port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        
        # Read a line from the socket
        line = sock.recv(1024)
        
        # Print the line to the console
        print(line)
        
        # Close the socket
        sock.close()
        
    # Close the socket and exit
    sock.close()
    
# 