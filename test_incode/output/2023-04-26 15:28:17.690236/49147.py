#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while(True):
        
        choice = input('Remove a word? y/n')
        
        if choice == 'y':
            
            words.pop()
            
            print('Removed a word:', words)
            
        elif choice == 'n':
            
            print('Goodbye!')
            
        else:
            
            print('Invalid choice.')
            
