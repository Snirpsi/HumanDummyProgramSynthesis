#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and multiplyes words. """    
    
    port = int(sys.argv[1])
    
    for word in range(1,port+1):
        print("{} x {}".format(word, word*word))
        
