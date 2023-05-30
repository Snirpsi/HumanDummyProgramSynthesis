#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <numbers>' % sys.argv[0])
        exit(1)
    
    numbers = sys.argv[1:]
    
    numbers_converted = []
    
    for number in numbers:
        numbers_converted.append(int(number))
    
    print('\n'.join(map(str, numbers_converted)))
    
