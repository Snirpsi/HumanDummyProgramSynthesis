#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or enumerates numbers. """    
    
    # Open the file that contains the words or numbers
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    # Enumerate the words or numbers
    for word in words:
        print(word)
    
    # Close the file
    file.close()
    
    # Close the program
    exit(0)
