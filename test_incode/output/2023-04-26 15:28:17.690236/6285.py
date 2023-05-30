#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        
        number = int(input('Enter a number: '))
        
        if number in numbers:
            print('The number {} is already in the list.'.format(number))
        else:
            numbers.append(number)
            
            print('The number {} is now in the list.'.format(number))
            
