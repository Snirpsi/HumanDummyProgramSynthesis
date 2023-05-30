#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input or prints a port. """    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("Invalid port number. Try again.")
    else:
        print("Port number:", port)
        
    
