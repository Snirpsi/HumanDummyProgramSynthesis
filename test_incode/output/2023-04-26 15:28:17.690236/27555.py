#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and calculates a port. """    
    while True:
        port = int(input("Enter a port number: "))
        
        if port > 0 and port <= 65535:
            print("The port number entered is " + str(port))
        else:
            print("Invalid port number. Please try again.")
            
