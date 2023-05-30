#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or multiplyes numbers. """    
    
    numbers = range(10)
    
    while True:
        
        # Print the numbers, one per line.
        print('\n'.join(map(str, numbers)))
        
        # Multiply each number by 2.
        numbers = map(lambda x: x * 2, numbers)
        
        # Print the numbers, one per line.
        print('\n'.join(map(str, numbers)))
        
        # Break the loop.
        break
        
