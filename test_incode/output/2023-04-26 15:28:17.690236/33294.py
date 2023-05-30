#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and stores words. """    
    
    # Open the port on which the webserver will listen
    port = 8080
    
    # Open a socket to listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    sock.bind(('0.0.0.0', port))
    
    # Listen for connections
    sock.listen(5)
    
    # Accept a connection
    print('[*] Listening on port ' + str(port))
    
    while True:
        # Accept a connection
        conn, addr = sock.accept()
        
        # Receive the request and print it
        data = conn.recv(1024)
        print(data.decode())
        
        # Close the connection
        conn.close()
        
        # Wait for a new request
        conn.recv(1024)
        
    # Close the socket
    sock.close()
    
    # Close the server
    