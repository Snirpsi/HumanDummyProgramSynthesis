#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and multiplyes words. """    
    import sys
    words = [word.strip() for word in sys.stdin.read().split(' ')]
    
    count = 0
    for word in words:
        count += int(word)
    
    print(count)

<|/ file filename=