#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and stores a list of words. """    
    
    words = []
    
    # Open a socket and listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    sock.listen(1)
    
    # Accept a connection and print its message
    while True:
        conn, addr = sock.accept()
        print('Received connection from', addr)
        
        # Receive the message and print it
        data = conn.recv(1024)
        print('Received "%s"' % data)
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        
        # Send the message back to the client
        conn.send(''.join(words))
        