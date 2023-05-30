#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        choice = input('\nEnter your choice: ')
        
        if choice == 'quit':
            break
        
        if choice in fruits:
            print(choice, 'is a fruit!')
        else:
            print(choice, 'is not a fruit!')
            
