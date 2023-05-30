#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or removes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port > 0 and port < 65536:
            print("Port number " + str(port) + " is open.")
        else:
            print("Invalid port number. Try again.")
