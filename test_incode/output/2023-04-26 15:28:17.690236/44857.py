#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and adds a list of words. """    
    while True:
        port = input('Enter a port number: ')
        words = []
        for i in range(10):
            words.append(input('Enter a word: ').capitalize())
        print('The words are:', words)
        print('The ports are:', 