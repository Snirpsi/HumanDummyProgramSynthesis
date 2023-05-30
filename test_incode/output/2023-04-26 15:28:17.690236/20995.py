#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    while True:
        port = input('Enter port number: ')
        
        # Open a socket to port number
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((port, 0))
        
        # Send a message to the socket
        sock.send('Hello World!')
        
        # Receive a message from the socket
        message = sock.recv(1024)
        
        # Close the socket
        sock.close()
        
        # Print the received message
        print('Received: ' + message)
        
        # Wait for user input
        input()
        
