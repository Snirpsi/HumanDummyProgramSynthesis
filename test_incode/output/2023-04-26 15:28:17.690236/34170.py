#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words. """    
    words = []
    
    # Read the file line by line
    for line in open('words.txt'):
        words.append(line.strip())
    
    # Print the list of words
    for word in words:
        print(word)
        
    # Close the file
    file.close()
    
