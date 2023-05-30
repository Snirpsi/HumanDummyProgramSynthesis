#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words and multiplyes all ports. """    
    ports = range(1,5)
    for port in ports:
        print('Starting port {}'.format(port))
        
        # Start a TCP server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', port))
        server.listen(1)
        print('Listening on port {}'.format(port))
        
        # Start a TCP client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', port))
        print('Connected to port {}'.format(port))
        
        # Send a message to server
        client.send('Hello World!')
        
        # Receive a message from server
        message = client.recv(1024)
        print('Received message from server: {}'.format(message))
        
        # Close the server
        client.close()
        server.close()
        
        print('Done.')
        
        # Wait for a message from the server
        message = client.recv(1024)
        print('Received message from server: {}'.format(message))
        
        # Close the server
        client.close()
        server.close()
        
        print('Done.')
        
        # Wait for a message from the server
        message = client.recv(1024)
        print('Received message from server: {}'.format(message))
        
        # Close the server
        client.close()
        server.close()
        
        print('Done.')
        
        # Wait for a message from the server
        message = client.recv(1024)
        print('Received message from server: {}'.format(message))
        
        # Close the server
        client.close()
        server.close()
        
        print('Done.')
        
        # Wait for a message from the server
        message = client.recv(1024)
        print('Received message from server: {}'.format(message))
        
        # Close the server
        client.close()
        server.close()
        
        print('Done.')
        
        # Wait for a message from the server
        message = client.recv(1024)
        print('Received message from server: {}'.format(message))
        
        # Close the server
        client.close()
        server.close()
        
        print('Done.')
        
        # Wait for a message from the server
        message = client.recv(1024)
        print('Received message from server: {}'.format(message))
        
        # Close the server
        client.close()
        server.close()
        
        print('Done.')
        
        # Wait for a message from the server
        message = client.recv(1024)
        print('Received message from server: {}'.format(message))
        
        # Close the server
        client.close()
        server.close()
        
        print('Done.')
        
        # Wait for a message from the server
        message = client.recv(1024)
        print('Received message from server: {}'.format(message))
        
        # Close the server
        client.close()
        server.close()
        
        print('Done.')
        
