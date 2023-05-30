#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    # Open the word file
    word_file = open('words.txt', 'r')
    
    # Read the words from the file
    words = word_file.readlines()
    
    # Close the word file
    word_file.close()
    
    # Print the words in the file
    print('\n'.join(words))
    
    # Close the file
