#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and multiplyes numbers. """    
    while True:
        port = input("Enter a port number: ")
        
        # Read port number from user
        port = int(port)
        
        # Multiply port number by 10
        port = 10 * port
        
        # Print port number
        print(port)
        
        # Wait for user to press enter to exit
        input()
        
