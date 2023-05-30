#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words and prints user input. """    
    
    # Read user input
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    
    # Print user input
    print('\n'.join(' '.join(words).split()))
    
    # Quit program
    print('Goodbye!')
    
