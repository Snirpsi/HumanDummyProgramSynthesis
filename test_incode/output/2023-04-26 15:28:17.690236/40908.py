#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and multiplyes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        number = input('Enter a number: ')
        
        if number == 'quit':
            break
        
        fruit = fruits[int(number)]
        
        print('The fruit is', fruit)
        
        print('Press enter to continue')
        
        input()
        
    print('Goodbye!')
    
