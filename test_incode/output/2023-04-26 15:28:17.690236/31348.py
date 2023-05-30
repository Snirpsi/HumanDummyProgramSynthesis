#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or calculates a list of numbers. """    
    words = ['cat', 'dog', 'mouse']
    numbers = [1, 2, 3, 4]
    
    while True:
        print('The words are:')
        for word in words:
            print(word)
        print('The numbers 