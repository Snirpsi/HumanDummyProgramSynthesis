#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    port = int(sys.argv[1])
    
    # Connect to port and print out its contents. 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    # Send a message to the server. 
    sock.send('Hello, world!')
    
    # Receive the server's response. 
    message = sock.recv(1024)
    
    # Close the connection. 
    sock.close()
    
    # Print the server's response. 
    print(message)
    
    # Close the connection. 
    sock.close()
    
    # Close the program. 
    sys.exit()
