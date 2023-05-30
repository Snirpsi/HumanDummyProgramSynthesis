#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input and enumerates a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
        
    print('The words are:')
    
    for word in words:
        print(word)
        
    print('')
    
    print('The word that occurs most often is', 
          word