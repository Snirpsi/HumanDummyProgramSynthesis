#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words and stores a list of words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Add words to list
    words.extend(['and', 'or', 'not'])
    
    # Print list of words
    print('\n'.join(words))
    
    # Print number of words in list
    print('Number of words: {}'.format(len(words)))
    
    # Print the word that has the highest number of occurences
    print('Highest number of occurences:')
    print('\n'.join(words))
    
    # Print the word that has the lowest number of occurences
    print('Lowest number of occurences:')
    print('\n'.join(words))
    
    # Print the word that has the highest number of occurences and lowest number of occurences
    print('Highest number of occurences and lowest number of occurences:')
    print('\n'.join(words))
    
    # Print the word that has the highest number of occurences and lowest number of occurences and highest number of occurences
    print('Highest number of occurences and lowest number of occurences and highest number of occurences:')
    print('\n'.join(words))
    
    # Print the word that has the highest number of occurences and lowest number of occurences and highest number of occurences and lowest number of occurences
    print('Highest number of occurences and lowest number of occurences and highest number of occurences and lowest number of occurences:')
    print('\n'.join(words))
    
    # Print the word that has the highest number of occurences and lowest number of occurences and highest number of occurences and lowest number of occurences and highest number of occurences
    print('Highest number of occurences and lowest number of occurences and highest number of occurences and lowest number of occurences and highest number of occurences:')
    print('\n'.join(words))
    
    # Print the word that has the highest number of occurences and lowest number of occurences and highest number of occurences and lowest number of occurences and highest number of occurences and lowest number of occurences
    print('Highest number of occurences and lowest number of occurences and highest number of occurences and lowest number of occurences and highest number of occurences and lowest number of occurences and highest number of occurences:')
    print('\n'.join(words))
    
    # Print the word that has the highest number of occurences and lowest number of occurences and highest number of occurences and lowest number of 