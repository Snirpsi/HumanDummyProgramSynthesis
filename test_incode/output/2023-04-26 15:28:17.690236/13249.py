#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        
        choice = input('Enter your choice: ')
        
        if choice == 'quit':
            break
        
        elif choice == '1':
            print('You chose option 1.')
            
        elif choice == '2':
            print('You chose option 2.')
            
        elif choice == '3':
            print('You chose option 3.')
            
        elif choice == '4':
            print('You chose option 4.')
            
        elif choice == '5':
            print('You chose option 5.')
            
        elif choice == 'quit':
            print('Goodbye!')
            
        else:
            print('Invalid choice.')
            
    print('Goodbye!')
    
