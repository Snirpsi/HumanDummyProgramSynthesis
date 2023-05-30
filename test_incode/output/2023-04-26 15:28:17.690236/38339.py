#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and returns user input. """    
    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Print all words to user
    print('\n'.join('%s ' % w for w in words))
    
    # Read user input
    word = ''
    while True:
        word = input('Enter a word: ')
        
        # Check if word is valid
        if word not in words:
            print('Sorry, that word is not in the list')
            continue
        
        # Print word and user input
        print('%s %s' % (word, words[words.index(word)]))
    
    # Close file
    f.close()
    
    # Close terminal
    terminal.close()
    
    # Close program
    