#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    
    words = []
    
    for line in sys.stdin:
        words.append(line.strip().lower())
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)
    
