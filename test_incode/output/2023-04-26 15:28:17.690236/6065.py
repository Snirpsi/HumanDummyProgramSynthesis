#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or removes fruits. """    
    words = ['apple', 'orange', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        choice = input('> ')
        
        if choice == 'quit':
            break
        
        if choice == 'remove':
            fruits.remove(fruits[0])
            
        elif choice == 'add':
            fruits.append(fruits[0])
            
        else:
            print('Invalid choice.')
            
    print('You chose:', fruits)
    
