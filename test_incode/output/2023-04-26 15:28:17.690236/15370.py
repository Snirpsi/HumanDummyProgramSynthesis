#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or enumerates words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        choice = input('Choose a number from 1-9: ')
        if choice == '':
            break
        else:
            print(words[int(choice)])
            
