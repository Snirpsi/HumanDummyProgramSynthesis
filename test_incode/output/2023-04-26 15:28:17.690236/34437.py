#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or converts user input. """    
    
    # Get the arguments from the command line
    args = sys.argv[1:]
    
    # Parse the arguments
    numbers = []
    for arg in args:
        numbers.append(int(arg))
    
    # Multiply all numbers
    total = 0
    for number in numbers:
        total += number
    
    # Print the result
    print(total)
    
