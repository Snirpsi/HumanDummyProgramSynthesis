#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and calculates all ports. """    
    
    port = 0
    while True:
        
        # Open a socket to the port and read from it
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Send the message and receive the response
        sock.send("Hello World!")
        response = sock.recv(1024)
        
        # Close the socket and print out the response
        sock.close()
        print("Received: %s" % response)
        
        # Increment the port number
        port += 1
        
        # Check if we're done
        if port == 65535:
            break
        
    # Close the socket and quit 