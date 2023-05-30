#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        words.append(input('Enter a word: '))
        
        print('The word was:', ', '.join(words))
        
        print('Would you like to add another word? (y/n)')
        
        choice = input('> ')
        
        if choice.lower() == 'y':
            words.append('pineapple')
            
            print('The word was:', ', '.join(words))
            
            print('Would you like to add another word? (y/n)')
            
            choice = input('> ')
            
            if choice.lower() == 'y':
                words.append('pineapple')
                
                print('The word was:', ', '.join(words))
                
                print('Would you like to add another word? (y/n)')
                
                choice = input('> ')
                
                if choice.lower() == 'y':
                    words.append('pineapple')
                
                    print('The word was:', ', '.join(words))
                
                    print('Would you like to add another word? (y/n)')
                
                    choice = input('> ')
                
                    if choice.lower() == 'y':
                        words.append('pineapple')
                
