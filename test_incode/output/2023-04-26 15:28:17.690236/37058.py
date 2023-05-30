#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input. """    
    
    choice = input('What would you like to do? ')
    
    if choice == '1':
        print('You chose to start a game')
        
    elif choice == '2':
        print('You chose to play again')
        
    elif choice == '3':
        print('You chose to quit game')
        
    else:
        print('Invalid choice')
        
    
