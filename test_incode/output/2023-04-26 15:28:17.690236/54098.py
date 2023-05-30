#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port. """    
    
    # Get the arguments from the command line
    port = int(sys.argv[1])
    
    # Create a socket and connect to the port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, port))
    
    # Send some data
    sock.send('Hello world!')
    
    # Receive some data
    data = sock.recv(1024)
    
    # Close the socket
    sock.close()
    
    # Print the received data
    print(data)
    
