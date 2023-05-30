#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and adds a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    
    print('\n'.join(words))
    
    print('\nTotal words: ', len(words))
    
    print('\nTotal letters: ', sum(len(word) for word in words))
    
    print('\nTotal digits: ', sum(len(word) for word in words))
    
    print('\nTotal words with digits: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with letters: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with spaces: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and letters: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and letters and spaces: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and letters and spaces and special characters: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and letters and spaces and special characters and digits: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and letters and spaces and special characters and digits and letters: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and letters and spaces and special characters and digits and letters and spaces: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and letters and spaces and special characters and digits and letters and spaces and special characters and digits and letters: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and letters and spaces and special characters and digits and letters and spaces and special characters and digits and letters and spaces: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and letters and spaces and special characters and digits and letters and spaces and special characters and digits and letters and spaces: ', sum(1 for word in words if len(word) > 1))
    
    print('\nTotal words with special characters and digits and 