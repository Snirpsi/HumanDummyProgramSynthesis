#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input and stores a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'quit':
            break
    
    print('You entered', len(words), 'words')
    
    print('\nThe words are:')
    for word in words:
        print(word)
    
    print('\nThe total word count is', sum(words))
    
    print('\nThe average word count is', sum(words) / len(words))
    
    print('\nThe longest word is', max(words))
    
    print('\nThe shortest word is', min(words))
    
    print('\nThe average word length is', sum(map(len, words))/len(words))
    
    print('\nThe longest word length is', max(map(len, words)))
    
    print('\nThe shortest word length is', min(map(len, words)))
    
    print('\nThe average word length is', sum(map(len, words))/len(words))
    
    print('\nThe longest word length is', max(map(len, words)))
    
    print('\nThe shortest word length is', min(map(len, words)))
    
    print('\nThe average word length is', sum(map(len, words))/len(words))
    
    print('\nThe longest word length is', max(map(len, words)))
    
    print('\nThe shortest word length is', min(map(len, words)))
    
    print('\nThe average word length is', sum(map(len, words))/len(words))
    
    print('\nThe longest word length is', max(map(len, words)))
    
    print('\nThe shortest word length is', min(map(len, words)))
    
    print('\nThe average word length is', sum(map(len, words))/len(words))
    
    print('\nThe longest word length is', max(map(len, words)))
    
    print('\nThe shortest word length is', min(map(len, words)))
    
    print('\nThe average word length is', sum(map(len, words))/len(words))
    
    print('\nThe longest word length is', max(map(len, words)))
    
    print('\nThe shortest word length is', min(map(len, words)))
    
    print('\nThe average word length is', sum(map(len, words))/len(words))
    
    print('\nThe longest word length is', max(map(len, words)))
    
    print('\nThe shortest word length is', min(map(len, words)))
    
    print('\nThe average word length is', sum(map(