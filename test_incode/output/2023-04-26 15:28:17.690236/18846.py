#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words and prints a list of numbers. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'snake', 'monkey']
    numbers = [1, 2, 3, 4, 5]
    
    for word, number in zip(words, numbers):
        print(word, number)
    
