#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and removes words. """    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    words = filter(lambda word: word not in words, words)
    
    for word in words:
        print(word)
        
    