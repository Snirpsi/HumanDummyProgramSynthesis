#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    words = []
    
    for i in range(port):
        words.append(str(i))
    
    print(" ".join(words))
    
