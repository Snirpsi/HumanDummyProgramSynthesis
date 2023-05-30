#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words or returns a list of words. """    
    words = ['foo', 'bar', 'baz']
    
    # Loop forever
    while True:
        # Multiply each word in the list
        words = [x * y for x, y in zip(words, words)]
        # Print the list
        print('\n'.join(words))
    
    # Loop until the user exits
    while True:
        # Read the user input
        choice = input('> ')
        # Exit the loop if the user enters quit
        if choice == 'quit':
            break
        # Otherwise do something else
        else:
            # Print the choice
            print('Invalid input')
    
    # Close the program 