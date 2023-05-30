#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['word1', 'word2', 'word3']
    
    i = 0
    while True:
        print(words[i])
        i += 1
        
        if i == len(words):
            break
        
        if i % 10 == 0:
            print('')
            
