#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and returns a list of words. """    
    
    words = removeWords(sys.argv[1])
    
    for word in words:
        print(word)
    
