#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    # Create a socket and connect to the specified port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', port))
    
    # Read all bytes from the socket and print them to the screen
    while True:
        data = sock.recv(1024)
        print(data)
    
    # Close the socket and clean up
    sock.close()
    
