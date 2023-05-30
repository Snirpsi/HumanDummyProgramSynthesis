#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <filename>' % sys.argv[0])
        sys.exit(1)
    
    filename = sys.argv[1]
    
    numbers = []
    with open(filename) as fp:
        for line in fp:
            numbers.append(int(line))
    
    numbers = list(set(numbers))
    numbers.sort()
    
    print('\n'.join(map(str, numbers)))
    
