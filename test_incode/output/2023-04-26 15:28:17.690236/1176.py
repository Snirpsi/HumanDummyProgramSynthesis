#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and calculates a list of numbers. """    
    
    # Get the port number
    port = int(sys.argv[1])
    
    # Get the list of numbers
    numbers = range(port)
    
    # Multiply each number by 10 and print it
    for number in numbers:
        print(number * 10)
    
