#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports and prints user input. """    
    ports = [int(port) for port in input().split()]
    
    # Multiply all ports
    for port in ports:
        ports[port] = ports[port] * 2
    
    # Print user input
    for port in ports:
        print(port)
        
    # Print the result
    for port in ports:
        print(ports[port])
        
    # Close the file
    file.close()
    
    # Close the program
    exit(0)
