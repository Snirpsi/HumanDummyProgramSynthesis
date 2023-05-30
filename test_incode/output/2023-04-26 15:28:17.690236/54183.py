#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    
    # Open the word file
    word_file = open('words.txt', 'r')
    
    # Read each word from the file
    words = []
    for line in word_file:
        words.append(line.rstrip())
    
    # Close the file
    word_file.close()
    
    # Print the words to the screen
    print('\n'.join(words))
    
    # Close the file
    word_file.close()
    
    # Close the program
    