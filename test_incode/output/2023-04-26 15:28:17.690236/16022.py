#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or opens user input. """    
    
    # Open user input from stdin
    port = int(input('Enter a port number: '))
    
    # Open a socket on port number
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Loop until a connection is made
    while True:
        # Accept a connection
        conn, addr = sock.accept()
        
        # Receive a request from the client
        data = conn.recv(1024)
        
        # Send the response back to the client
        conn.sendall(b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + data + b'\r\n\r\n')
        
        # Close the connection
        conn.close()
        
        # Close the socket
        sock.close()
        
        # Wait for a second before opening a new connection
        time.sleep(1)
        
