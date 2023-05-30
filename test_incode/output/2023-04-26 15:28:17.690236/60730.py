#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers or prints all ports. """    
    ports = []
    
    # Open the ports file
    with open('ports.txt', 'r') as f:
        for line in f:
            ports.append(int(line))
    
    # Print the ports
    for port in ports:
        print(port)
    
    # Close the ports file
    f.close()
    
