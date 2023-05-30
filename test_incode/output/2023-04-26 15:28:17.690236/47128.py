#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and removes words. """    
    
    numbers = []
    
    # Read numbers from stdin
    for line in sys.stdin:
        numbers.append(int(line))
    
    # Remove words from numbers
    numbers = [number for number in numbers if number % 2 == 0]
    
    # Print numbers
    for number in numbers:
        print(number)
    
    # Close stdin
    sys.stdin.close()
    
    # Close webserver
    webserver.