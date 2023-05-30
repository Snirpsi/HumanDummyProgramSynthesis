#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <numbers>' % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1].split(',')
    
    numbers_str = ''
    for number in numbers:
        numbers_str += str(number) + ' '
    
    print('\n'.join(numbers_str.split(' ')))
