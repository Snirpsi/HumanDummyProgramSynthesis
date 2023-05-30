#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and enumerates all ports. """    
    
    port = 8080
    
    # Open a socket to the port and listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Loop forever
    while True:
        # Accept a connection and read its content
        conn, addr = sock.accept()
        
        # Print the received message
        print('Received a connection from {}'.format(addr))
        
        # Send the message to the client
        conn.sendall('Hello, world!\n')
        
        # Close the connection
        conn.close()
        
        # Wait a little bit before continuing
        time.sleep(0.1)
