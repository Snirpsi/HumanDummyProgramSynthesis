#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and calculates a list of words. """    
    port = int(sys.argv[1])
    words = []
    for i in range(1, port+1):
        words.append(str(i))
    print(" ".join(words))
    
