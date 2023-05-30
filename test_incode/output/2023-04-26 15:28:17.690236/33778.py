#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input and iterates over all ports. """    
    ports = []
    
    ports.append(input('Enter the port number of the server to connect to: '))
    ports.append(input('Enter the port number of the client to connect to: '))
    
    ports.reverse()
    
    for port in ports:
        
        print('Connecting to port {} ...'.format(port))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((port, 