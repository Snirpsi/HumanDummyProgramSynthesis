#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or opens a port. """    
    port = int(sys.argv[1])
    
    # Open a socket to listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Accept connection and handle it
    client, addr = sock.accept()
    while True:
        data = client.recv(1024)
        if not data: break
        
        # Send the received data back to the client
        client.sendall(data)
        
        # Close the client socket
        client.close()
    
    # Close the socket and exit
    sock.close()

<|/ file ext=.py source=github |>