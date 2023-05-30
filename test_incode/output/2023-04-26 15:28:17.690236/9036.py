#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or adds a list of numbers. """    
    port = '/dev/ttyACM0'
    
    # Open the port and read its content
    file = open(port, 'r')
    
    # Iterate over each line of the file
    for line in file:
        # Split the line into individual numbers
        numbers = line.strip().split()
        
        # Print the numbers
        print(numbers)
        
    # Close the file
    file.close()
    
    # Close the port
    file.close()
    
    # Close the terminal
    