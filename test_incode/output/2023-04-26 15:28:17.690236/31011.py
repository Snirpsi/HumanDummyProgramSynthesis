#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or converts numbers. """    
    while True:
        word = input('Enter a word: ')
        number = int(input('Enter a number: '))
        if word == 'quit':
            break
        elif word == 'stop':
            break
        else:
            print(word, number)
            
