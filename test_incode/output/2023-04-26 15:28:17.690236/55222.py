#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers. """    
    
    # Get the numbers from the command line
    numbers = sys.argv[1:]
    
    # Multiply them all together
    total = 0
    for number in numbers:
        total += number
    
    # Print the result
    print(total)
    
    # 