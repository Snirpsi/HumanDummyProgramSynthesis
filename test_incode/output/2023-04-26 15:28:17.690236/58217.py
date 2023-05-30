#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    words = []
    
    for i in range(1, port + 1):
        words.append(str(i) + "*")
    
    print(" ".join(words))
    
