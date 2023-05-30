#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['foo', 'bar', 'baz']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('\nDo you wish to continue? [y/N] ')
        
        if choice.lower() == 'y':
            break
        
        else:
            print('\nGoodbye!')
            
