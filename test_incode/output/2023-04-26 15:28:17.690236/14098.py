#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = int(sys.argv[1])
    
    # Open the port and print out its contents
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        client, addr = sock.accept()
        print('Got connection from', addr)
        
        # Receive the request from the client
        data = client.recv(1024)
        print('Received "%s"' % data)
        
        # Send the response back to the client
        client.send(data)
        
        # Close the connection
        client.close()
        
