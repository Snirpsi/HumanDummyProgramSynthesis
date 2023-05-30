#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words and removes a list of words. """    
    while True:
        words = input('Enter a word: ')
        words = words.split()
        words.extend(words)
        words = list(set(words))
        words.sort()
        print(' '.join(words))
        
        if words == ['exit']:
            break
        
        print('Enter another word: ')
        
