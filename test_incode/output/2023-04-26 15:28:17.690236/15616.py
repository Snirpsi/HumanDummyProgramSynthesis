#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and enumerates all ports. """    
    
    # Create a socket and bind to all available interfaces
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 0))
    s.listen(1)
    
    # Listen for connections
    while True:
        c, addr = s.accept()
        print('Connected by', addr)
        
        # Receive the request and send it to the client
        c.send(b'GET / HTTP/1.0\r\n\r\n')
        c.close()
        
        # Receive the response and send it to the client
        data = c.recv(1024)
        c.send(b'HTTP/1.0 200 OK\r\n\r\n' + data + b'\r\n\r\n')
        c.close()
        
        # Close the connection
        c.close()
        
        # Wait for another request
