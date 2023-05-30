#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports. """    
    
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    sock.bind(('', 8888))
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Accept the incoming connection
    client, addr = sock.accept()
    
    # Receive the message and print it
    print('Received message:', 