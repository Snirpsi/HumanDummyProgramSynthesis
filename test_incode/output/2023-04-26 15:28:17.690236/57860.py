#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers and enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'rabbit', 'lion', 'snake', 'monkey']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('\nEnter a number from 0 to 5 to exit: ')
        
        if choice == '0':
            break
        
        if choice == '1':
            word = 'cat'
            
        elif choice == '2':
            word = 'dog'
            
        elif choice == '3':
            word = 'mouse'
            
        elif choice == '4':
            word = 'rabbit'
            
        elif choice == '5':
            word = 'lion'
            
        else:
            print('Invalid input')
            
        words.append(word)
        
    print('\nThe words are:')
    
    for word in words:
        print(word)
    
    print('\nThe number is:', choice)
    
