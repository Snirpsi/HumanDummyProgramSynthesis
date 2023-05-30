#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    if len(numbers) == 0:
        print('Usage: %s [numbers]' % sys.argv[0])
        exit(1)
    
    numbers = map(int, numbers)
    
    numbers = list(map(lambda x: x * x, numbers))
    
    print('\n'.join(map(str, numbers)))
    
