#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and converts a list of numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    if len(numbers) == 0:
        print('Usage: python -m webserver numbers')
        sys.exit()
    
    numbers = [int(x) for x in numbers]
    
    print('Content-type: text/html')
    
    for number in numbers:
        print('<p>{}</p>'.format(number))
    
    print('