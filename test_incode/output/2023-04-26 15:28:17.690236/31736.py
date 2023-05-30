#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and stores words. """    
    
    # Read user input
    words = []
    while True:
        word = input('Enter a word: ')
        if not word:
            break
        words.append(word)
    
    # Print the results
    print('Words: ', words)
    
    # Close the program
    print('Goodbye!')
    
