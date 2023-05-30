#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    words = []
    
    for word in wordlist:
        words.append(word.lower())
        
    words = ' '.join(words)
    
    print(words)
    
