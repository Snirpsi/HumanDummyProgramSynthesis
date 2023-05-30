#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and stores a list of words. """    
    port = int(sys.argv[1])
    words = []
    for i in range(port):
        words.append(sys.argv[2])
    print(" ".join(words))
    
