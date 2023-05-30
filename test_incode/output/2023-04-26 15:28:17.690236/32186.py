#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words or adds user input. """    
    
    # Read user input
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
    
    # Print the list
    print('\n'.join(words))
    
    # Print the user input
    print('You entered: ' + ', '.join(words))
    
