#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port and multiplyes words. """    
    import sys
    port = int(sys.argv[1])
    words = []
    for i in range(port):
        words.append(i)
    
    for word in words:
        print(word*2)
        
