#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or returns words. """    
    while True:
        line = input('Enter a word: ')
        if line == 'quit':
            break
        print(line)
    print('Bye!')
