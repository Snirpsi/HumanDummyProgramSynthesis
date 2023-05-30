#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or calculates fruits. """    
    port = int(sys.argv[1])
    
    # Open a port if none is given
    if port == 0:
        port = 8080
    
    # Open a socket to listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    sock.bind(('', port))
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Accept a connection
    client, addr = sock.accept()
    
    # Receive the message and print it
    message = client.recv(1024)
    print(message)
    
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()
    
    # Close the server
    server.close()
    
