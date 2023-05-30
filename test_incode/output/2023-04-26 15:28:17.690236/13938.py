#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and adds a port. """    
    
    # Open a port on localhost
    port = int(sys.argv[1])
    
    # Open a socket on port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    # Accept connections
    client, addr = sock.accept()
    
    # Read all bytes from the client
    data = client.recv(1024)
    
    # Print the received data
    print(data.decode())
    
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()

<|/ file source=github dstars=1 |>