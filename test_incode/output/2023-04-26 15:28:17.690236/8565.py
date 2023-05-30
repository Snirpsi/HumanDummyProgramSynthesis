#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or iterates over a list of numbers. """    
    
    # Get the list of numbers from stdin
    numbers = sys.stdin.read().split()
    
    # Iterate over the numbers and print them out
    for number in numbers:
        print(number)
        
    # 