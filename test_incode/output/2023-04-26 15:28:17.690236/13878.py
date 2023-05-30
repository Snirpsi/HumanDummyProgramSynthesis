#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or converts numbers. """    
    while True:
        word = input('Enter a word: ')
        number = input('Enter a number: ')
        if word == 'exit':
            break
        if number == 'exit':
            break
        if word.isdigit():
            print(int(number))
        else:
            print(word)
