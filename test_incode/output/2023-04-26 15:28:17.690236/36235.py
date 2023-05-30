#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or stores fruits. """    
    
    fruits = []
    
    # Iterate over all ports
    for port in range(1,25):
        
        # Open a connection to the port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Send a message to the port
        sock.send('Hello world')
        
        # Receive a message from the port
        message = sock.recv(1024)
        
        # Append the received message to the fruits list
        fruits.append(message)
        
        # Close the connection
        sock.close()
    
    # Print the fruits list
    print(fruits)
    
    # Close the socket
    sock.close()
    
    # Close the program
    sys.exit()
    
