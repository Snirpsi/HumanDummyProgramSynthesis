#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    
    words = ['cat', 'dog', 'bird', 'mouse']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('\nEnter a choice: ')
        
        if choice == 'quit':
            break
        
        else:
            choice = int(choice)
            
            if choice == 1:
                word = 'cat'
            elif choice == 2:
                word = 'dog'
            elif choice == 3:
                word = 'bird'
            elif choice == 4:
                word = 'mouse'
                
            print(word)
            
