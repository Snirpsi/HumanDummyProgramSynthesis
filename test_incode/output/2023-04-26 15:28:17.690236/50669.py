#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    numbers = []
    
    for word in words:
        numbers.append(int(word))
    
    print('\n'.join(map(str, numbers)))
    
