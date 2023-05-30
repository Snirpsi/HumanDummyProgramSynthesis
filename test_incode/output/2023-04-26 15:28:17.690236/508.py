#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or enumerates a list of numbers. """    
    port = int(sys.argv[1])
    
    # Open a socket to listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Listen for connections
    while True:
        conn, addr = sock.accept()
        
        # Receive the request and print it
        data = conn.recv(1024)
        print('Received request from {}'.format(addr))
        
        # Send the response back to the client
        conn.send('OK')
        
        # Close the connection
        conn.close()
        
