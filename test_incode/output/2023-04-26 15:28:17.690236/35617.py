#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    words = []
    
    # Read in the file of words and store them in the list 'words'
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Print the list of words to the screen
    print('\n'.join(words))
    
    # Print the length of the list
    print('Length of list: {}'.format(len(words)))
    
    # Print the average length of the list
    print('Average length of list: {}'.format(sum(map(len, words))/len(words)))
    
    # Print the average length of the list divided by the number of words in the list
    print('Average length of list divided by the number of words in the list: {}'.format(sum(map(len, words))/len(words)))
    
    # Print the average length of the list divided by the number of words in the list divided by the number of words in the list
    print('Average length of list divided by the number of words in the list divided by the number of words in the list: {}'.format(sum(map(len, words))/len(words))/len(words)))
    
    # Print the average length of the list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list
    print('Average length of list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list: {}'.format(sum(map(len, words))/len(words))/len(words))/len(words))
    
    # Print the average length of the list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list
    print('Average length of list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list: {}'.format(sum(map(len, words))/len(words))/len(words))/len(words))/len(words))
    
    # Print the average length of the list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list
    print('Average length of list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list divided by the number of words in the list: {}'.format(sum(map(len, words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))/len(words))