#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or opens words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word == '':
            continue
        
        words.append(word)
        
    print('\n'.join(words))
    
