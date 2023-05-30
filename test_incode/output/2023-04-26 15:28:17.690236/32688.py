#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or iterates over words. """    
    while True:
        line = input('Enter a word: ')
        if line == 'quit':
            break
        else:
            print(line)
