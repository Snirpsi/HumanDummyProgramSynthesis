#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers or iterates over a port. """    
    
    # Remove a list of numbers
    remove_numbers(['1', '2', '3'])
    
    # Iterate over a port
    port = '/dev/ttyUSB0'
    for number in remove_numbers(port):
        print(number)
