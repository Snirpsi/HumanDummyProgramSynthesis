#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input or prints fruits. """    
    
    fruits = input('Enter your favorite fruits: ')
    
    if fruits == 'apple':
        print('Apple')
    elif fruits == 'orange':
        print('Orange')
    elif fruits == 'banana':
        print('Banana')
    elif fruits == 'cherry':
        print('Cherry')
    elif fruits == 'pineapple':
        print('Pineapple')
    else:
        print('Unknown fruit')
        
