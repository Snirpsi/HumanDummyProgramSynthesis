#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port and adds fruits. """    
    
    # Create a list to hold the fruits
    fruits = []
    
    # Open a port and enumerate its contents
    port = serial.Serial('/dev/ttyUSB0', 9600)
    
    # Iterate over each character in the port
    for c in port.read(1):
        # Append the character to the list
        fruits.append(c)
    
    # Close the port
    port.close()
    
    # Print the fruits list
    print('\n'.join(fruits))
    
