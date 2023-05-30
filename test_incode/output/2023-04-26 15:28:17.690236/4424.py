#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and prints a list of numbers. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'bird', 'cat']
    numbers = [1, 2, 3, 4, 5]
    
    for word in words:
        for number in numbers:
            print(word, number)
    
