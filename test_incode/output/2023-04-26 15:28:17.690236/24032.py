#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words or returns numbers. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # enumerate words and numbers
    for word, number in zip(words, numbers):
        print(word, number)
    
    # enumerate words and numbers in reverse order
    for number, word in enumerate(reversed(words), start=1):
        print(number, word)
    
    # enumerate words and numbers in reverse order and print in reverse order
    for number, word in enumerate(reversed(words), start=1):
        print(number, word, sep=' ')
    
    # enumerate words and numbers in reverse order and print in reverse order and print in reverse order
    for number, word in enumerate(reversed(words), start=1):
        print(number, word, sep=' ', end=' ')
    
    # enumerate words and numbers in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse order and print in reverse 