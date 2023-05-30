#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words or stores a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s word" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    wordlist = word.split()
    
    multiplier = 1
    
    for word in wordlist:
        multiplier = multiplier * int(word)
    
    print(multiplier)
    
