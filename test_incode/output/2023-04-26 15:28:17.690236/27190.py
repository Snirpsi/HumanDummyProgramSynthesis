#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    # Print the words in the list
    print(words)
    
    # Print the length of the list
    print(len(words))
    
    # Print the length of the first word
    print(len(words[0]))
    
    # Print the length of the last word
    print(len(words[-1]))
    
    # Print the length of the first and last word
    print(len(words[0]) + len(words[-1]))
    
    # Print the length of the first and last word and store it in a variable
    lengths = 