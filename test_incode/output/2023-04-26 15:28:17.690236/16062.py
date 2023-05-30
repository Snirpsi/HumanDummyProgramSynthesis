#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports or adds user input. """    
    
    # Get the port number from command line or user input
    port = int(input("Enter the port number: "))
    
    # Multiply all ports
    ports = port * 2
    
    # Add user input
    ports += int(input("Enter the port number: "))
    
    # Print the result
    print("The ports multiplied by 2 are: " + str(ports))
    
    # Close the program
    quit()
    
