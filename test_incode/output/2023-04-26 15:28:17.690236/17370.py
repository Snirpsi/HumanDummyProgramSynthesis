#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers or iterates over words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python add.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    word