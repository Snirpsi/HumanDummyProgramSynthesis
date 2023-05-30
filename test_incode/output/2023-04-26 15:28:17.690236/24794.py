#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    while True:
        print('\n'.join('%s %s' % (w, w) for w in words))
        
        choice = input('\nEnter a choice: ')
        
        if choice == 'quit':
            print('Goodbye!')
            break
        
        if choice == 'cat':
            print('You chose cat.')
            
        elif choice == 'dog':
            print('You chose dog.')
            
        elif choice == 'mouse':
            print('You chose mouse.')
            
        elif choice == 'bird':
            print('You chose bird.')
            
        else:
            print('Sorry, I did not understand your choice.')
            
