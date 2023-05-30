#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or opens words. """    
    port = int(sys.argv[1])
    
    words = []
    
    # Open a socket to listen for connections
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server.bind(('', port))
    
    # Listen for incoming connections
    server.listen(5)
    
    # Accept the connection and make a connection
    client, address = server.accept()
    
    # Send the client a welcome message
    message = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: text/html\r\n'
               '\r\n')
    client.send(message)
    
    # Receive the response and print it
    while True:
        data = client.recv(1024)
        if not data: break
        
        # Send the response back to the client
        client.send(data)
    
    # Close the connection
    client.close()
    
    # Send the client a message indicating that all words have been sent
    message = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: text/html\r\n'
               '\r\n')
    client.send(message)
    
    # Close the connection
    client.close()
    
    # Send the client a message indicating that all words have been sent
    message = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: text/html\r\n'
               '\r\n')
    client.send(message)
    
    # Close the connection
    client.close()
    
    # Send the client a message indicating that all words have been sent
    message = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: text/html\r\n'
               '\r\n')
    client.send(message)
    
    # Close the connection
    client.close()
    
    # Send the client a message indicating that all words have been sent
    message = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: text/html\r\n'
               '\r\n')
    client.send(message)
    
    # Close the connection
    client.close()
    
    # Send the client a message indicating that all words have been sent
    message = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: text/html\r\n'
               '\r\n')
    client.send(message)
    
    # Close the connection
    client.close()
    
    # Send the client a message indicating that all words have been sent
    message = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: text/html\r\n'
               '\r\n')
    client.send(message)
    
    # Close the connection
    client.close()
    
    # Send the client a message indicating that all words have been sent
    message = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: text/html\r\n'
               '\r\n')
    client.send(message)
