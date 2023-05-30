#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or stores words. """    
    
    words = []
    
    while True:
        
        # Read a word from the user
        word = input('Enter a word: ')
        
        # Append the word to the words list
        words.append(word)
        
        # Print the word list to the user
        print('Your word list is: ', end='')
        print('\n'.join(words))
        
        # Break the loop when the user hits CTRL-C
        if word == 'quit':
            break
        
    # Print the word list to the user
    print('Your word list is: ', end='')
    print('\n'.join(words))
    
    # Close the program when the user hits CTRL-C
