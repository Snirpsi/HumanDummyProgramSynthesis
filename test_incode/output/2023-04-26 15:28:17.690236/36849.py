#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    words = []
    
    # Open the file containing the list of words and read it into a list.
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    # Print the list of words to the terminal.
    print('\n'.join(words))
    
    # Close the file.
    words.close()
    
    # Close the terminal.
    