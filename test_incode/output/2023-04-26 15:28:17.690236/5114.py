#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and stores numbers. """    
    
    # Open the port on the local machine
    port = int(sys.argv[1])
    
    # Open a socket to listen on that port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    # Accept connections
    client, addr = sock.accept()
    
    # Receive a message from the client
    message = client.recv(1024).decode()
    
    # Send a message back to the client
    client.send(message.encode())
    
    # Close the client socket
    client.close()
    
    # Close the server socket
    sock.close()
    
