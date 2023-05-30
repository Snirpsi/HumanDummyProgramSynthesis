#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    port = int(sys.argv[1])
    
    # Open a socket to the specified port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    # Send a message to the socket
    s.send("Hello, world!")
    
    # Receive the message from the socket
    message = s.recv(1024)
    
    # Close the socket
    s.close()
    
    # Print the received message
    print(message)
    
    # Close the socket and exit the program
    s.close()
    sys.exit()
    
    
