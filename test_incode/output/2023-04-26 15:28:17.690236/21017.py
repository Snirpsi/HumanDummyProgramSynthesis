#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    while True:
        words = input('Enter a word: ')
        words = [word.strip() for word in words.split()]
        
        multiplied = []
        for word in words:
            multiplied.append(word*2)
        
        print(' '.join(multiplied))
        
