#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    ports = []
    
    # Open a socket and listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(5)
    
    # Accept connections
    while True:
        conn, addr = sock.accept()
        
        # Receive the message and print it
        data = conn.recv(1024)
        
        # Send the message back to the client
        conn.send('OK')
        
        # Close the connection
        conn.close()
        
        # Add the port to the list
        ports.append(addr)
        
        # Print the port number
        print('Port number ' + str(addr[0]) + ': ' + addr[1])
        
        # Close the socket
        sock.close()
    
    # Close the socket
    sock.close()
    
    # Print the list of ports
    print('Ports:')
    for port in ports:
        print('\t' + str(port))
    
    print('\nDone.')
    
