#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or removes a list of numbers. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        
        choice = input('Enter a word or number: ')
        
        if choice == 'exit':
            break
        
        elif choice == 'remove':
            
            words.remove(choice)
            
            print('Removed word:', choice)
            
        elif choice == 'removeall':
            
            words = []
            
            print('Removed all words')
            
        else:
            
            print('Invalid input')
            
    print('Done')
    
