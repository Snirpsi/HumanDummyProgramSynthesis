#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports and returns fruits. """    
    
    # Open the ports
    ports = openPorts()
    
    # Convert all ports
    fruits = convertPorts(ports)
    
    # Close the ports
    ports.close()
    
    # Print the fruits
    printFruits(fruits)
    
    # Close the fruits.
    fruits.close()
    
    # Close the program
    exit(0)
    
# Run the program
main()

<|/ file ext=.py source=github |>