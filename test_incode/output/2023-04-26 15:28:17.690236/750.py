#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and returns a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    
    # Create a socket and bind to port 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    # Accept a connection and read a line of text
    client, addr = sock.accept()
    
    # Read a line of text and split it into numbers
    while True:
        data = client.recv(1024)
        if not data: break
        numbers.append(int(data))
    
    # Close the socket
    client.close()
    
    # Print the list of numbers
    print('\n'.join(str(n) for n in numbers))
    
    # Close the server
    sock.close()

<|/ file filename=server.py ext=.py source=github |>