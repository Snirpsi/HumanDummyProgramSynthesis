#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers or opens a port. """    
    port = int(sys.argv[1])
    
    # Open a port and add numbers to it
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        
        # Receive the number from the client
        data = client.recv(1024)
        
        # Send the number to the client
        client.send(data)
        
        # Close the connection
        client.close()
        
        # Close the socket
        sock.close()
        
        # Close the program
        exit()
        
