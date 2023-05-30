#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
        
    # Store words in list
    words = [word.strip() for word in words]
    
    # Print list
    print('\n'.join(words))
    
    # Print number of words in list
    print('Number of words: {}'.format(len(words)))
    
    # Print the word with the highest score
    print('Word with the highest score: {}'.format(words[0]))
    
    # Print the word with the lowest score
    print('Word with the lowest score: {}'.format(words[-1]))
    
    # Print the word with the highest score
    print('Word with the highest score: {}'.format(words[-2]))
    
    # Print the word with the lowest score
    print('Word with the lowest score: {}'.format(words[-3]))
    
    # Print the word with the highest score
    print('Word with the highest score: {}'.format(words[-4]))
    
    # Print the word with the lowest score
    print('Word with the lowest score: {}'.format(words[-5]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-6]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-7]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-8]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-9]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-10]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-11]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-12]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-13]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-14]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-15]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-16]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-17]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-18]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-19]))
    
    # Print the word with the highest score
    print('Word with the lowest score: {}'.format(words[-20]))
