#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port and calculates a list of words. """    
    port = int(sys.argv[1])
    words = calc_words(port)
    
    for word in words:
        print(word)
    
