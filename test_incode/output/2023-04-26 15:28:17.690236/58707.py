#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and multiplyes user input. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        print('\nEnter a number to multiply by')
        number = int(input())
        
        if number == 0:
            break
        
        fruit = fruits[number-1]
        
        print('\nThe fruit is', fruit)
        
        print('\nDo you want to continue? y/n')
        answer = input()
        
        if answer == 'y' or answer == 'Y':
            break
        
    print('\nGoodbye!')
    
