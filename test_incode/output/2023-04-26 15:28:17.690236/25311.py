#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = sys.stdin.readline()
    
    words = []
    
    for _ in range(number):
        words.append(sys.stdin.readline())
    
    print(" ".join(words))
    
