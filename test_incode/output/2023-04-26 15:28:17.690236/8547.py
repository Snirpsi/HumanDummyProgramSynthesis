#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or iterates over a port. """    
    while True:
        words = []
        
        # Read a line from the input file
        line = input('Enter a word: ')
        
        # Append the word to the list of words and print it out
        words.append(line)
        
        # Print the list of words to the screen
        print('\n'.join(words))
        
        # Check if the user wants to quit the program
        quit = input('Do you want to quit (y/n)? ')
        
        # Quit if the user enters anything other than 'y' or 'n'
        if quit not in ('y', 'n'):
            print('Invalid input. Exiting...')
            
            # Break the loop
            break
        
        # Print a message to the user and ask if they want to enter another word
        print('Enter another word: ')
        
        # Append the word to the list of words and print it out
        words.append(input(''))
        
        # Print the list of words to the screen
        print('\n'.join(words))
        
        # Check if the user wants to quit the program
        quit = input('Do you want to quit (y/n)? ')
        
        # Quit if the user enters anything other than 'y' or 'n'
        if quit not in ('y', 'n'):
            print('Invalid input. Exiting...')
            
            # Break the loop
            break
        
        # Print a message to the user and ask if they want to enter another word
        print('Enter another word: ')
        
        # Append the word to the list of words and print it out
        words.append(input(''))
        
        # Print the list of words to the screen
        print('\n'.join(words))
        
        # Check if the user wants to quit the program
        quit = input('Do you want to quit (y/n)? ')
        
        # Quit if the user enters anything other than 'y' or 'n'
        if quit not in ('y', 'n'):
            print('Invalid input. Exiting...')
            
            # Break the loop
            break
        
        # Print a message to the user and ask if they want to enter another word
        print('Enter another word: ')
        
        # Append the word to the list of words and print it out
        words.append(input(''))
        
        # Print the list of words to the screen
        print('\n'.join(words))
        
        # Check if the user wants to quit the program
        quit = input('Do you want to quit (y/n)? ')
        
        # Quit if the user enters anything other than 'y' or 'n'
        if quit not in ('y', 'n'):
            print('Invalid input. Exiting...')
            
            # Break the loop
            break
        
        # Print a message to the 