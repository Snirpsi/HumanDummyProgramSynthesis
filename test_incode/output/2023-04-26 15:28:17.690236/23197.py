#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or stores fruits. """    
    
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    sock.connect((HOST, PORT))
    
    # Send the message to the server
    sock.send(MESSAGE)
    
    # Receive the message from the server
    message = sock.recv(BUFFER_SIZE)
    
    # Close the socket
    sock.close()
    
    # Print the message received
    print(message)
    
    # Close the socket
    sock.close()
    
    # Close the program
    exit(0)
    
