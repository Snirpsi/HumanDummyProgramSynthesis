#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and prints words. """    
    
    words = []
    
    # Open the file containing the list of words and read it line by line
    for line in open('words.txt'):
        line = line.strip()
        words.append(line)
    
    # Print the words in the file to the screen
    print('\n'.join(words))
    
    # Close the file
    