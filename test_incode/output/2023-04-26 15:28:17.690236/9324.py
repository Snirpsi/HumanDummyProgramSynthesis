#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    ports = []
    
    # Create a server socket and bind it to all available interfaces
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 0))
    
    # Listen for incoming connections
    server.listen(10)
    
    # Listen for connections
    while True:
        # Accept a connection
        conn, addr = server.accept()
        
        # Print the port number
        print('[+] Listening on port {}'.format(addr[1]))
        
        # Add the port to the list
        ports.append(addr[1])
        
        # Close the connection
        conn.close()
        
        # Wait a second
        time.sleep(5)
        
    # Close the server
    server.close()
    
    # Print the ports
    print('[+] Ports listened: {}'.format(ports))
    
    # Close the socket
    server.close()
    
    # Close the program
    sys.exit(0)
    
