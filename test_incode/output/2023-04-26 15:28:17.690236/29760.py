#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input or returns a list of words. """    
    
    # Get the user input
    words = []
    while True:
        word = input('Enter a word: ')
        if not word:
            break
        words.append(word)
    
    # Multiply user input or return list of words
    if words:
        print('The words are:')
        for word in words:
            print(word)
    else:
        print('No words found')
    
    # Print the list of words
    print('The list of words are:')
    for word in words:
        print(word)
    
    # Print the list of words with spaces
    print('The list of words are:')
    for word in words:
        print(word)
    
    # Print the list of words with spaces
    print('The list of words are:')
    for word in words.