#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or calculates a port. """    
    
    # Open the file that contains the list of numbers
    file = open('numbers.txt', 'r')
    
    # Read the numbers from the file
    numbers = file.readlines()
    
    # Close the file
    file.close()
    
    # Print the list of numbers
    print('\n'.join(numbers))
    
    # Calculate a port
    port = int(input('Enter a number: '))
    
    # Print the port
    print('The port is', port)
    
    # Close the file
    file.close()
    
    # Close the program
    exit(0)
    
    # 