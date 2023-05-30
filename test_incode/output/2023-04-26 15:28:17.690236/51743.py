#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words. """    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)
    
