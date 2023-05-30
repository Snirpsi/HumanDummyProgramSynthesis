#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        
        # Multiply port by 2
        port *= 2
        
        # Print the new port number
        print("The new port number is {}".format(port))
        
        # Wait for user to press enter to exit
        input()
        
        # Exit the loop
        break
        
