#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words and enumerates a list of numbers. """    
    words = ['cat', 'dog', 'mouse']
    numbers = [1, 2, 3, 4]
    
    # Print the words and numbers in alphabetical order.
    print('Words:', words)
    print('Numbers:', numbers)
    
    # Print the words and numbers in numerical order.
    print('Words in numerical order:')
    for number in numbers:
        print(number, end=' ')
    print()
    
    # Print the words and numbers in numerical order and in alphabetical order.
    print('Words in numerical order and in alphabetical order:')
    for number, word in zip(numbers, words):
        print(number, word, end=' ')
    print()
    
    # Print the words and numbers in numerical order and in alphabetical order and in alphabetical order.
    print('Words in numerical order and in alphabetical order and in alphabetical order:')
    for number, word, zipped in zip(numbers, words, zipped):
        print(number, word, zipped)
    print()
    
    # Print the words and numbers in numerical order and in alphabetical order and in alphabetical order and in alphabetical order.
    print('Words in numerical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order:')
    for number, word, zipped, zipped in zip(numbers, words, zipped, zipped):
        print(number, word, zipped, zipped)
    print()
    
    # Print the words and numbers in numerical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in alphabetical order and in 