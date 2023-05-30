#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words or iterates over a port. """    
    port = int(sys.argv[1])
    
    # Open a socket to the port and receive a message
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, port))
    
    # Send a message to the port and receive a response
    message = b"Hello, world!"
    s.send(message)
    response = s.recv(1024)
    s.close()
    
    # Print the response to the user
    print(response)
    
    # Close the socket
    s.close()
    
