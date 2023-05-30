#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    ports = []
    
    # Open a socket for each available port
    for port in range(0, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        ports.append(port)
    
    # Listen for connections
    while True:
        client, addr = sock.accept()
        print('Connected by', addr)
        
        # Listen for connections
        while True:
            data, addr = client.recvfrom(1024)
            print('Received', len(data), 'bytes')
            
            # Send the data
            client.sendall(data)
            
            # Close the connection
            client.close()
            
