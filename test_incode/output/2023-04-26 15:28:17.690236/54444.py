#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and removes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        
        if port == 9999:
            print("Goodbye!")
            break
        else:
            print("You entered a port number", port, "