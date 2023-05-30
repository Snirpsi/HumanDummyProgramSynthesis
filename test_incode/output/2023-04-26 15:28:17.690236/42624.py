#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and iterates over all ports. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        for fruit in fruits:
            print('The fruit is', fruit)
        
        choice = input('\nPlease select an option: ')
        
        if choice == 'quit':
            break
        
        elif choice == 'a':
            print('You chose apple')
            
        elif choice == 'b':
            print('You chose banana')
            
        elif choice == 'c':
            print('You chose cherry')
            
        else:
            print('Sorry, I did not understand your choice.')
            
