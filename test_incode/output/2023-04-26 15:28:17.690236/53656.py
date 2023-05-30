#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or calculates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[0]
    
    numbers = []
    
    for word in words:
        numbers.append(int(word))
    
    print('\n'.join(map(str, numbers)))
    
