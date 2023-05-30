#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates user input and opens words. """    
    
    # Open the word list
    word_list = open('words.txt', 'r')
    
    # Read and print the words from the word list
    words = word_list.readlines()
    
    # Close the word list
    word_list.close()
    
    # Print the words to the screen
    print('\n'.join(words))
    
    # Close the program
    