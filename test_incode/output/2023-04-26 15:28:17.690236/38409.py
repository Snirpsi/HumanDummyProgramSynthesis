#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input and removes words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(word)
            
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

<|/ file filename=word