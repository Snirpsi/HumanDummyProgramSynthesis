#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or converts words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        number = int(input('Enter a number: '))
        print(number, word)
        
