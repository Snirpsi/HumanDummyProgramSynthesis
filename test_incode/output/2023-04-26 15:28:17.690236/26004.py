#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or multiplyes words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        for word in words:
            print(word*2)
    else:
        print('Usage: python3 