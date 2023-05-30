#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        word = input('Enter a word: ')
        if word in words:
            words.remove(word)
        else:
            print('That word is not in the list')
            
