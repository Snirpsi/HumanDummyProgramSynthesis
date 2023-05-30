#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers and enumerates fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        number = input('Enter a number: ')
        
        if number == 'q':
            break
        
        if number in fruits:
            print(number, end='\t')
        else:
            print('Invalid number, try again.')
    
    print('Thanks for playing!')
    
