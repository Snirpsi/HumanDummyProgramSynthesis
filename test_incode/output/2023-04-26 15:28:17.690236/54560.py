#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and opens user input. """    
    while True:
        words = []
        
        while True:
            word = input('Enter a word: ')
            
            if word == 'q':
                break
            
            words.append(word)
        
        print('\n'.join(words))
        
        answer = input('Do you want to continue? [y/N] ')
        
        if answer == 'y':
            break
        
    print('Goodbye!')
