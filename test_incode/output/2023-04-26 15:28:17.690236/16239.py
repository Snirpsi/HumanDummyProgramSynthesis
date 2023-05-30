#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    while True:
        
        word = ''.join(words)
        
        print('{} * {} = {}'.format(word, word, word*word))
        
        words.pop(0)
        
        if len(words) == 0:
            break
        
        time.sleep(1)
        
