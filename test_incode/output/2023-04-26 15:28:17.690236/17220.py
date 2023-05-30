#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input and iterates over a list of words. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    
    print('\n'.join([word for word in words]))
    
