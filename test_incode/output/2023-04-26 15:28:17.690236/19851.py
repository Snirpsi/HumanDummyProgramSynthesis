#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Open the file that contains the words and read them into a list
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    # Print the list of words to the user
    print('\n'.join(words))
    
    # Close the file
    file.close()
    
    # Return the list of words to the user
    return words

