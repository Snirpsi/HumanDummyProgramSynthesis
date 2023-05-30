#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    # Open a port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(1)
    
    # Wait for a connection
    client, addr = sock.accept()
    
    # Send some data
    client.send('Hello, world!'.encode())
    
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()
    
