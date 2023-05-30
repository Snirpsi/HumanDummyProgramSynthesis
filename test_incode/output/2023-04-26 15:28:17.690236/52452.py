#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input and multiplyes a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
        
        print('The word is', word)
        
    print('The final word is', ' '.join(words))
    
    print('Thanks for playing!')
    
