#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words. """    
    
    words = []
    
    # Read a word from a file
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    # Print the word list
    print('\n'.join(words))
    
    # Print the length of the word list
    print('Length of word list: ' + str(len(words)))
    
    # Print the average length of the word list
    print('Average length of word list: ' + str(round(sum(map(len, words))/len(words), 2)))
    
    # Print the average length of the word list with punctuation
    print('Average length of word list with punctuation: ' + str(round(sum(map(len, words))/len(words)*100, 2)))
    
    # Print the average length of the word list with punctuation with spaces
    print('Average length of word list with punctuation with spaces: ' + str(round(sum(map(len, words))/len(words)*100, 2)))
    
    # Print the average length of the word list with punctuation with spaces and 