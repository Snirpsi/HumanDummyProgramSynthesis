#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and converts numbers. """    
    
    # Get the list of words and convert them to numbers
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [int(word) for word in words]
    
    # Print the numbers in the list
    print('Numbers:')
    print(numbers)
    
    # Print the words in the list
    print('Words:')
    print(words)
    
    # Print the words and numbers in the list
    print('Words and numbers:')
    print(words + numbers)
    
    # Print the words and numbers in the list with spaces between them
    print('Words and numbers with spaces between them:')
    print(words + numbers + [' '])
    
    # Print the words and numbers in the list with spaces between them and with a comma
    print('Words and numbers with spaces between them and with a comma:')
    print(words + numbers + [' ', ','])
    
    # Print the words and numbers in the list with spaces between them and with a comma and a space
    print('Words and numbers with spaces between them and with a comma and a space:')
    print(words + numbers + [' ', ',', ' '])
    
    # Print the words and numbers in the list with spaces between them and with a comma and a space and another comma
    print('Words and numbers with spaces between them and with a comma and a space and another comma:')
    print(words + numbers + [' ', ',', ' ', ','])
    
    # Print the words and numbers in the list with spaces between them and with a comma and a space and another comma and a space
    print('Words and numbers with spaces between them and with a comma and a space and another comma and a space:')
    print(words + numbers + [' ', ',', ' ', ',', ' ', ','])
    
    # Print the words and numbers in the list with spaces between them and with a comma and a space and another comma and a space and another comma
    print('Words and numbers with spaces between them and with a comma and a space and another comma and a space and another comma and a space:')
    print(words + numbers + [' ', ',', ' ', ',', ' ', ',', ' ', ',', ' ', ','])
    
    # Print the words and numbers in the list with spaces between them and with a comma and a space and another comma and a space and another comma and a space and another comma
    print('Words and numbers with spaces between them and with a comma and a space and another comma and a space and another comma and a space and another comma and a space:')
    print(words + numbers + ['