#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or enumerates words. """    
    words = ['word1', 'word2', 'word3']
    
    word_counter = 0
    
    for word in words:
        word_counter += 1
        
        if word_counter % 2 == 0:
            print(word)
        else:
            print(word.upper())
            
