#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or removes a list of numbers. """    
    words = ['hello', 'world', '123', '456', '789']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        elif word in words:
            print('The word ' + word + ' is awesome!')
        elif word in numbers:
            print('The number ' + word + ' is awesome!')
        else:
            print('That word or number is not recognized. Try again.')
    
    print('Goodbye!')
    
