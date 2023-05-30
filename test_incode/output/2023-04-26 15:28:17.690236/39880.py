#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port and iterates over all ports. """    
    
    # Open a port and start listening for incoming connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(1)
    
    # Create a thread to listen for connections.
    threading.Thread(target=listen, args=(sock,)).start()
    
    # Create a thread to accept connections.
    threading.Thread(target=accept, args=(sock,)).start()
    
    # Wait for connections.
    while True:
        # Accept a connection and print its remote address.
        conn, addr = sock.accept()
        print('Connection from %s' % repr(addr))
        
        # Send a message to the client and print its response.
        print('Send a message')
        conn.send('Hello world')
        
        # Receive a message from the client and print its response.
        print('Receive a message')
        data = conn.recv(1024)
        print('Received: %r' % data)
        
        # Close the connection.
        conn.close()
        
        # Send a message to the client and print its response.
        print('Send a message')
        conn.send('Bye bye')
        
        # Receive a message from the client and print its response.
        print('Receive a message')
        data = conn.recv(1024)
        print('Received: %r' % data)
        
        # Close the connection.
        conn.close()
        
        # Send a message to the client and print its response.
        print('Send a message')
        conn.send('Bye bye')
        
        # Receive a message from the client and print its response.
        print('Receive a message')
        data = conn.recv(1024)
        print('Received: %r' % data)
        
        # Close the connection.
        conn.close()
        
        # Send a message to the client and print its response.
        print('Send a message')
        conn.send('Bye bye')
        
        # Receive a message from the client and print its response.
        print('Receive a message')
        data = conn.recv(1024)
        print('Received: %r' % data)
        
        # Close the connection.
        conn.close()
        
        # Send a message to the client and print its response.
        print('Send a message')
        conn.send('Bye bye')
        
        # Receive a message from the client and print its response.
        print('Receive a message')
        data = conn.recv(1024)
        print('Received: %r' % data)
        
        # Close the connection.
        conn.close()
        
        # Send a message to the client and print its response.
        print('Send a message')
        conn.send('Bye bye')
        
        # Receive a 