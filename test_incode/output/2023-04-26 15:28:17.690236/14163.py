#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers and multiplyes words. """    
    while True:
        number = int(input('Enter a number: '))
        word = input('Enter a word: ')
        
        number = number * word
        
        print('The number multiplied by the word is', number)
        
        if number == 