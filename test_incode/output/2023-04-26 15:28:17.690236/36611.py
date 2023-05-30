#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        numbers = map(int, sys.argv[1:])
        
        numbers = list(numbers)
        
        numbers.extend(numbers)
        
        print(numbers)
    else:
        print("Usage:")
        print("  python add_numbers.py <numbers>")
        print("Example:")
        print("  python add_numbers.py 1 2 3 4 5")
        
