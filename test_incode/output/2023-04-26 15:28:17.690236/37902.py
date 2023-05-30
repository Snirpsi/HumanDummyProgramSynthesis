#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers and converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <file> [<file> ...]' % sys.argv[0])
        sys.exit()
    
    for filename in sys.argv[1:]:
        with open(filename, 'r') as f:
            numbers = map(int, f.readlines())
            
        for number in numbers:
            print(number + 