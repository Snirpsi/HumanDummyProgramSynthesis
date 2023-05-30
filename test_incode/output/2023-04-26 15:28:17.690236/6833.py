#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and converts a port. """    
    
    # Read user input
    port = int(input("Enter a port number: "))
    
    # Convert port
    port = convert_port(port)
    
    # Print result
    print("The port number is", port)
    
    # Close program
    exit()
    
