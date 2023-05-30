#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words and prints user input. """    
    
    # Read user input
    words = []
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        # Check if user wants to quit
        if word == 'quit':
            break
    
    # Print user input
    print('\n'.join(words))
    
    # Quit program
    print('Goodbye!')
    
