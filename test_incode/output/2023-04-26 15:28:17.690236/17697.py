#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        choice = input('Choose a fruit from the list: ')
        
        if choice == 'quit':
            break
        
        elif choice in fruits:
            print('You chose ' + choice)
        else:
            print('That fruit 