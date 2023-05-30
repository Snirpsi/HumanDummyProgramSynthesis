#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits. """    
    
    fruits = ['apple', 'orange', 'pear', 'banana', 'kiwi']
    
    while True:
        fruits.append(input('Enter a fruit: '))
        
        print('You entered the following fruits:')
        print(fruits)
        
        print('Do you want to continue? [y/n]')
        
        choice = input('> ')
        
        if choice == 'y':
            break
        
        print('Goodbye!')
        
    print('Thanks for playing!')
    
