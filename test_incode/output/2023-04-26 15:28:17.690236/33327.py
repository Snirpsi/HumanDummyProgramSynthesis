#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers or multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 %s <words>" % sys.argv[0])
        exit()
    
    words = sys.argv[1].split()
    
    for word in words:
        print(word*