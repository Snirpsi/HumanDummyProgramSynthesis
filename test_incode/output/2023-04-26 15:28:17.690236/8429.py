#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits and iterates over user input. """    
    
    fruits = ['apple', 'banana', 'cherry', 'orange', 'pear']
    
    while True:
        
        fruit = input('Enter a fruit: ')
        
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print('Sorry, I don\'t know that fruit.')
            
        print('The fruit is', fruit)
        
        print('The fruits are now', fruits)
        
        print('Would you like to try again? Y/N')
        
        answer = input('> ')
        
        if answer == 'Y' or answer == 'y':
            
            break
            
        else:
            print('Thanks for playing!')
            
    print('Thanks for playing!')
    
