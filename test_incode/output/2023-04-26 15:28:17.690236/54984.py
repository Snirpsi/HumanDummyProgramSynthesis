#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and returns all ports. """    
    ports = []
    
    # Open a socket to listen for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(1)
    
    # Accept connections.
    while True:
        conn, addr = sock.accept()
        ports.append(addr)
        
        # Send the response to the client.
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send('Content-Type: text/html\r\n')
        conn.send('\r\n')
        conn.send('<h1>Hello World!</h1>\r\n')
        conn.send('\r\n')
        
        # Close the connection.
        conn.close()
        
        # Wait for a response.
        conn.send('GET / HTTP/1.1\r\n')
        conn.send('Host: localhost\r\n')
        conn.send('\r\n')
        
        # Receive the response.
        response = conn.recv(1024)
        
        # Send the response back to the client.
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send('Content-Type: text/html\r\n')
        conn.send('\r\n')
        conn.send('<h1>Hello World!</h1>\r\n')
        conn.send('\r\n')
        
        # Close the connection.
        conn.close()
        
        # Wait for a response.
        conn.send('GET / HTTP/1.1\r\n')
        conn.send('Host: localhost\r\n')
        conn.send('\r\n')
        
        # Receive the response.
        response = conn.recv(1024)
        
        # Send the response back to the client.
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send('Content-Type: text/html\r\n')
        conn.send('\r\n')
        conn.send('<h1>Hello World!</h1>\r\n')
        conn.send('\r\n')
        
        # Close the connection.
        conn.close()
        
        # Wait for a response.
        conn.send('GET / HTTP/1.1\r\n')
        conn.send('Host: localhost\r\n')
        conn.send('\r\n')
        
        # Receive the response.
        response = conn.recv(1024)
        
        # Send the response back to the client.
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send('Content-Type: text/html\r\n')
        conn.send('\r\n')
        conn.send('<h1>Hello World!</h1>\r\n')
        conn.send('\r\n')
        
        # Close the connection.
        conn.close()
        
        # Wait for a response.
        conn.send('GET / HTTP/1.1\r\n')
        conn.send('Host: localhost\r\n')
        conn.send('\r\n')
        
        # Receive the response.
        response = conn.recv(1024)
        
        # Send the response back to the client.
        conn.send('