#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    ports = []
    
    # Open a socket to listen on all available ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind to the port
    sock.bind(('localhost', 0))
    
    # Listen for connections
    sock.listen(1)
    
    # Accept connections
    while True:
        connection, client_address = sock.accept()
        
        # Send the client a message
        connection.send('Hello World!\n')
        
        # Send the client a message
        connection.send('Bye World!\n')
        
        # Close the connection
        connection.close()
        
        # Append the port to the list of ports
        ports.append(client_address[0])
        
        # Close the socket
        sock.close()
        
        # Print the ports
        print('Port numbers: %s' % ports)
        
        # Wait a second
        time.sleep(1)
        
