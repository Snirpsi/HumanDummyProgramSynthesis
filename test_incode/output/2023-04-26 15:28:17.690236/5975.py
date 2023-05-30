#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers and adds words. """    
    import sys
    
    numbers = list(map(int, sys.stdin.read().split()))
    words = list(map(str, sys.stdin.read().split()))
    
    numbers = numbers * len(words)
    
    sys.stdout.write(''.join(map(str, numbers)))
    sys.stdout.write('\n')
    
    for word in words:
        sys.stdout.write(word + ' ')
    
    sys.stdout.write('\n')
    
