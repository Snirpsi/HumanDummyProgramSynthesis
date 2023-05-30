#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input and iterates over a port. """    
    port = int(input("Enter a port number: "))
    
    # Remove user input
    port = str(input("Enter a port number: "))
    
    # Iterate over port
    for port in range(1, int(port)+1):
        print(port)
        
    # Close port
    