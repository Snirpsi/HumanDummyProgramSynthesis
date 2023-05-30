#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    # Open a port on which to listen
    port = int(sys.argv[1])
    
    # Open a socket to listen on port and accept connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Accept connection and print out the request
    conn, addr = sock.accept()
    
    # Receive the request and print it out
    conn.send('HTTP/1.1 200 OK\r\n')
    conn.send('Content-Type: text/html\r\n')
    conn.send('\r\n')
    
    # Receive the response and print it out
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send('Content-Type: text/html\r\n')
        conn.send('\r\n')
        
        # Send the response to the client
        conn.send(data)
    
    # Close the connection
    conn.close()
    
    # Close the socket
    sock.close()
    
