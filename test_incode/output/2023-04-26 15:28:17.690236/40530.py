#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and multiplyes user input. """    
    words = []
    
    # Read words from file
    for line in open('words.txt'):
        words.append(line.strip())
    
    # Print the multiplication table
    for word in words:
        print(word*