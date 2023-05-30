#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or prints words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        for word in words:
            print(word*2)
    else:
        print('Usage: python 