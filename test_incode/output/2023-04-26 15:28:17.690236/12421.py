#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words and stores numbers. """    
    words = ['cat', 'dog', 'mouse', 'elephant']
    numbers = []
    for word in words:
        numbers.append(word.count('