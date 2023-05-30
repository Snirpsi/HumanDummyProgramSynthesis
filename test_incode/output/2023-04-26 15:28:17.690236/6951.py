#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input and converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = list(map(int, numbers))
    
    numbers = remove_user_and_convert(numbers)
    
    print(numbers)
    
