#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or calculates numbers. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        number = int(word)
        print('The number is', number)
        
