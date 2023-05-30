#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input or stores words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'quit':
            break
        
    print('The words are:')
    
    for word in words:
        print(word)
    
    print('\nThe word that occurs most often is:', words[words.count(max(words))])
    
    print('\nThe word that occurs least often is:', words[words.count(min(words))])
    
    print('\nThe word that occurs most often and least often is:', words[words.count(max(words), min(words))])
    
    print('\nThe word that occurs most often and least often and most common is:', words[words.count(max(words), min(words)), words.count(max(words), min(words))])
    
    print('\nThe word that occurs least often and least often and most common is:', words[words.count(min(words), max(words)), words.count(min(words), max(words))])
    
    print('\nThe word that occurs least often and least often and least common is:', words[words.count(min(words), max(words)), words.count(min(words), max(words))])
    
    print('\nThe word that occurs most often and least often and least common and most common is:', words[words.count(max(words), min(words)), words.count(max(words), min(words)), words.count(max(words), min(words))])
    
    print('\nThe word that occurs least often and least often and least common and most common is:', words[words.count(min(words), max(words)), words.count(min(words), max(words)), words.count(min(words), max(words))])
    
    print('\nThe word that occurs most often and least often and least common and least common is:', words[words.count(max(words), min(words)), words.count(max(words), min(words)), words.count(max(words), min(words)), words.count(max(words), min(words))])
    
    print('\nThe word that occurs least often and least often and least common and least common is:', words[words.count(min(words), max(words)), words.count(min(words), max(words)), words.count(min(words), max(words)), words.count(min(words), max(words))])
    
    print('\nThe word that occurs most often and least often and least common and least common and least common is:', words[words.count(max(words), min(words)), words.count(max(words), min(words)), words.count(min(words), max(words))