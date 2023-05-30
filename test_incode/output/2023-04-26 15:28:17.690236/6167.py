#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or enumerates a list of numbers. """    
    
    # Print the list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for number in numbers:
        print(number)
    
    # Print the list of words
    words = ['cat', 'dog', 'mouse']
    for word in words:
        print(word)
    
    # Print the list of words and numbers
    words_and_numbers = ['cat', 'dog', 'mouse', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for word, number in zip(words, numbers):
        print(word, number)
    
    # Print the list of words and numbers and a space
    words_and_numbers_and_space = ['cat', 'dog', 'mouse', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ' ']
    for word, number, space in zip(words, numbers, ' '):
        print(word, number, space)
    
    # Print the list of words and numbers and a space and another word
    words_and_numbers_and_space = ['cat', 'dog', 'mouse', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ' ', 