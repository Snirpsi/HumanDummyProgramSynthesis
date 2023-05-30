#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and prints a port. """    
    port = int(sys.argv[1])
    
    # Open a socket and listen on port 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    
    # Accept a connection
    client, addr = sock.accept()
    
    # Print the port number
    message = client.recv(1024)
    
    # Close the socket
    client.close()
    
    # Print the message received
    print(message)
    
    # Close the socket
    sock.close()
    
    # Close the server
    server.close()
    
