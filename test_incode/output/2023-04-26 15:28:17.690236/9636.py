#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words or removes all ports. """    
    import sys
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv
    
    for word in words:
        word = word.strip()
        
        if len(word) > 0:
            print(word*