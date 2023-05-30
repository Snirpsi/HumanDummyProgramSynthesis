#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words and enumerates a list of words. """    
    words = sys.argv[1:]
    words = list(set(words))
    words.sort()
    words = enumerate(words)
    for word, index in words:
        print(word, index)
    
