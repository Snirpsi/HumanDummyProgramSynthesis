#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and calculates user input. """    
    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Print list of words
    print('\n'.join(words))
    
    # Calculate user input
    word = ''
    
    # Read user input
    while True:
        word = input('Enter a word: ')
        
        # Check if word is valid
        if word not in words:
            print('Invalid word')
            continue
        
        # Print word and user input
        print('{} : {}'.format(word, words[words.index(word)]))
        
        # Check if user input is valid
        if words[words.index(word)] != word:
            print('Invalid input')
            continue
        
        # Break loop
        break
    
    # Close file
    f.close()
    
    # Print result
    print('{} : {}'.format(word, words[words.index(word)]))
    
    # Close program
    sys.exit()
