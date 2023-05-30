#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words. """    
    while True:
        words = input('Enter a word: ').split()
        words.sort()
        print('Sorted words are: ')
        for word in words:
            print(word)
        print('')
        
