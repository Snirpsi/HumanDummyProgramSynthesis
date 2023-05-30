#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or returns user input. """    
    ports = enumerate_ports()
    
    # Print the ports found
    for port in ports:
        print('Found port {}'.format(port))
    
    # Get the user input
    port = input('Enter a port number: ')
    
    # Print the port number
    print('Found port {}'.format(port))
    
    # Close the server
    server.socket.close()
    
