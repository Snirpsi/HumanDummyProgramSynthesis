#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = 'apple'
        
        if fruit == 'cherry':
            print('You chose cherry.')
            break
        
        else:
            fruit = input('What fruit do you want? ')
            
            if fruit == 'apple':
                print('You chose apple.')
                break
            
            else:
                print('Sorry, I did not understand your choice.')
    
    print('Thank you for playing!')
    
