#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and converts fruits. """    
    
    # Create a socket and bind to port 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 5005))
    
    # Listen for connections
    sock.listen(1)
    
    while True:
        # Accept a connection
        conn, addr = sock.accept()
        
        # Convert the fruit
        fruit = 'apple'
        
        # Send the fruit to the client
        conn.send(fruit)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response
        print('Received: %s' % resp)
        
        # Close the connection
        conn.close()
        
        # Wait for a response
        resp = conn.recv(1024)
        
        # Print the response