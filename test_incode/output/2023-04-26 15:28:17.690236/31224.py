#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words and enumerates fruits. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        
        fruits = enumerate(''.join(word))
        for fruit in fruits:
            print('{} 