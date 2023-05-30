#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and enumerates numbers. """    
    words = ['cat', 'dog', 'mouse', 'chicken', 'bird', 'cat', 'dog', 'mouse', 'chicken', 'bird']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    i = 0
    while i < len(words):
        print('{} {}'.format(words[i], numbers[i]))
        i += 1
    
    print('Done.')
    
