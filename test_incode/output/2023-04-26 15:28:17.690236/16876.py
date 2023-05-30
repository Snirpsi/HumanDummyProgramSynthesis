#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or removes a port. """    
    
    words = []
    
    # Read a word or port
    while True:
        word = input('Enter a word or port:')
        
        # Remove a port
        if word[0].isdigit():
            words.remove(int(word))
        else:
            words.append(word)
    
    # Print the list
    print('\n'.join(words))
    
    # Close the program
    input('Press enter to exit')
    
