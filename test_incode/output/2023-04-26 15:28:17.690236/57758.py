#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    # Open the port and print its content
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(1)
    sock, addr = sock.accept()
    
    # Print the content
    sock.sendall(b'Hello, world!\n')
    
    # Close the port
    sock.close()
    
    # Close the socket
    sock.close()
    
