#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = []
    
    # Open a port for communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(1)
    ports.append(sock.getsockname()[1])
    
    # Wait for connection
    while True:
        client, addr = sock.accept()
        
        # Print all ports
        for port in ports:
            print(port)
        
        # Send the client a message
        client.send('Hello world!')
        
        # Close the connection
        client.close()
