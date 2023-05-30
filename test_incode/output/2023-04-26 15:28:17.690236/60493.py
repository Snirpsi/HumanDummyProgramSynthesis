#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input and prints a port. """    
    port = int(input("Enter a port number: "))
    
    # Open a socket and connect to the port number
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((str(port), 0))
    
    # Send a message to the socket
    s.send("Hello World!")
    
    # Receive a message from the socket
    msg = s.recv(1024)
    print(msg)
    
    # Close the socket
    s.close()
    
    # Close the program
    sys.exit()
