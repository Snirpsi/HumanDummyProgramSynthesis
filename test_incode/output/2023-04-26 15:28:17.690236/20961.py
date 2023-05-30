#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or iterates over words. """    
    while True:
        line = input('> ')
        if line == 'exit':
            break
        words = line.split()
        for word in words:
            print(word)
        print('')
