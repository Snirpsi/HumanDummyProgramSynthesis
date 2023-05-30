#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and iterates over a port. """    
    while True:
        port = int(input("Enter a port number: "))
        
        # Multiply user input by port number
        multiplier = port * port
        
        # Print the result
        print("The port multiplied by {} is {}".format(port, multiplier))
        
        # Wait for user input
        input("Press Enter to continue...")
        
        # Break out of the loop
        break
