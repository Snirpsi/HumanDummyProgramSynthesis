#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and opens fruits. """    
    
    # Open the ports
    ports = openports()
    
    # Open the fruits
    fruits = openfruits(ports)
    
    # Close the ports
    ports.close()
    
    # Close the fruits
    fruits.close()
    
    # Print the results
    print("Ports:")
    for port in ports:
        print(port)
    print("Fruits:")
    for fruit in fruits:
        print(fruit)
    
    
