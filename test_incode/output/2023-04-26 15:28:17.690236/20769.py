#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or stores numbers. """    
    while True:
        line = input('Enter a word: ')
        if line == 'quit':
            break
        else:
            print(line)
