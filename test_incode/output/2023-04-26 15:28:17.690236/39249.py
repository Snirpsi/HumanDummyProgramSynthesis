#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input and multiplyes words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    
    multiplied = []
    for word in words:
        multiplied.append(word*2)
    
    print('\n'.join(multiplied))
