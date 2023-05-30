#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port and prints a list of numbers. """    
    
    # Create a port to remove
    port = input('Enter a port number: ')
    
    # Remove a port
    remove_port(port)
    
    # Print the list of numbers
    numbers = list_numbers(port)
    
    # Print the list of numbers
    print('\n'.join(numbers))
    
