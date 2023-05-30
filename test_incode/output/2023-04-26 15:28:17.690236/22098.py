#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and adds words. """    
    
    words = []
    
    while True:
        
        line = input('Enter a word: ')
        
        if line == 'quit':
            break
        
        words.append(line)
        
    print('\n'.join(words))
    
    print('\n