#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits or enumerates numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        number = input('Enter a number: ')
        
        if number == 'done':
            break
        
        if number in fruits:
            print(number)
        else:
            print('Invalid input')
            
