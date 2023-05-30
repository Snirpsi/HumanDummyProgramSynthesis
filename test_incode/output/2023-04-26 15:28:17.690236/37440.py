#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or prints a list of numbers. """    
    
    # Open the file containing the words or numbers
    words = []
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    # Print the words or numbers to the screen
    print('\n'.join(words))
    
    # Close the file
    file.close()
    
    # Close the program
    exit(0)
