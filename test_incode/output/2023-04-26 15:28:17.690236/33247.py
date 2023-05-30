#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <filename>' % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    numbers = read_numbers(filename)
    
    numbers_str = ','.join(map(str, numbers))
    
    sys.stdout.write(numbers_str)
    
