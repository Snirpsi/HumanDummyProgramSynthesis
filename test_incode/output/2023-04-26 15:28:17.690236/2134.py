#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    while True:
        port = input('Enter a port number: ')
        
        # Open a socket and send some data
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((port, 0))
        sock.sendall(b'Hello, world!')
        
        # Receive some data from the server
        data = sock.recv(1024)
        
        # Print received data
        print('Received', repr(data))
        
        # Close the socket
        sock.close()
        
        # Wait for a key press
        print('Press any key to exit')
        
        # Wait for a key press
        