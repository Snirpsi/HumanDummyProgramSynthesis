#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and enumerates a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    for word in range(1,port+1):
        words.append(str(word))
        
    print(" ".join(words))
    
