#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    port = sys.argv[1]
    
    # Open a socket to the specified port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    # Send the request and receive the response
    sock.send("GET / HTTP/1.0\r\n\r\n")
    response = sock.recv(1024)
    
    # Close the socket
    sock.close()
    
    # Print the response
    print(response)
    
    # Close the connection
    sock.close()
    
    # Close the program
    sys.exit()
    
