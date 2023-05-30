#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    while True:
        words.pop()
        
        if words:
            print(' '.join(words))
        else:
            print('Done.')
            
        
