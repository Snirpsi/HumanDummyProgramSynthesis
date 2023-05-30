#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words or adds user input. """    
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word == 'add':
            print('Adding word: ' + word)
            
            words = []
            
            while True:
                word = input('Enter a word: ')
                
                if word == 'quit':
                    break
                
                words.append(word)
            
            print('Words: ' + ', '.join(words))
            
        elif word == 'list':
            print('Words: ' + ', '.join(words))
            
        else:
            print('Invalid command')
            
    print('Goodbye')
    
