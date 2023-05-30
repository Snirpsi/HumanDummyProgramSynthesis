#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates user input and stores words. """    
    
    # Read user input
    words = []
    
    # Read user input
    while True:
        word = input('Enter a word: ')
        
        # Check if word is valid
        if word != '' and word != '-':
            words.append(word)
        else:
            print('Invalid input')
            
        # Check if word is empty
        if word == '':
            print('Empty input')
            break
            
    # Print user input
    for word in words:
        print(word)
        
    # Print number of words
    print('Number of words: ', len(words))
    
    # Print longest word
    print('Longest word: ', max(words))
    
    # Print shortest word
    print('Shortest word: ', min(words))
    
    # Print average word
    print('Average word: ', sum(words) / len(words))
    
    # Print number of vowels
    print('Number of vowels: ', len(set(''.join(words)).