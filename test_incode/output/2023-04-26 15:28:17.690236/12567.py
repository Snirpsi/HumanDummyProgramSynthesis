#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or enumerates words. """    
    import sys
    if len(sys.argv) > 1:
        number = sys.argv[1]
    else:
        number = 1
    
    words = []
    
    for i in range(number):
        words.append(str(i))
    
    print(" ".join(words))
    
