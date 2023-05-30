#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or converts a list of words. """    
    
    words = []
    
    # Open a text file containing words and add them to the list
    file = open('words.txt', 'r')
    words = file.read().split()
    file.close()
    
    # Convert words to lower case
    words = [word.lower() for word in words]
    
    # Print the list of words
    print('Words:')
    for word in words:
        print(word)
    
    # Print the list of words in lower case
    print('\nWords in lower case:')
    for word in words:
        print(word.lower())
    
    # Print the list of words in all lower case
    print('\nWords in all lower case:')
    for word in words:
        print(word.upper())
    
    # Print the list of words in all upper case
    print('\nWords in all upper case:')
    for word in words:
        print(word.upper())
    
    # Print the list of words in all lower case and all upper case
    print('\nWords in all lower case and all upper case:')
    for word in words:
        print(word.upper(), word.lower())
    
    # Print the list of words in all lower case and all upper case and all lower case
    print('\nWords in all lower case and all upper case and all lower case:')
    for word in words:
        print(word.upper(), word.lower(), word.upper())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    