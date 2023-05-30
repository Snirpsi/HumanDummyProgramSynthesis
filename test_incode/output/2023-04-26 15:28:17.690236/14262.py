#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or calculates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world']
    
    numbers = []
    for word in words:
        numbers.append(int(word))
    
    print('\n'.join(map(str, numbers)))
    
