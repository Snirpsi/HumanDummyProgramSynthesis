#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['word1', 'word2', 'word3']
    
    while True:
        words.append('word4')
        
        print(words)
        
        time.sleep(1)
        
