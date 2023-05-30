#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    s.connect((HOST, port))
    
    # Send a message to the server
    s.send("Hello, world!")
    
    # Receive a message from the server
    message = s.recv(1024)
    
    # Print the received message
    print(message)
    
    # Close the socket
    s.close()
    
    # Close the connection
    s.shutdown(socket.SHUT_WR)
    
    # Close the server
    s.close()
    
    # Close the terminal
    