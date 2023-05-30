#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or enumerates a list of numbers. """    
    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    while True:
        number = input('Enter a number: ')
        
        if number in numbers:
            print('The number is', number)
        else:
            print('The number is', numbers[number])
            
        print('Press enter to exit')
        
        input()
        
