#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words or converts a list of numbers. """    
    
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        
        number = input('Enter a number: ')
        
        if number.isdigit():
            number = int(number)
            
            if number in numbers:
                number = number * 10
                
                print('The number you entered is {}!'.format(number))
                
            else:
                print('Sorry, that number is not in the list!')
                
        elif number.isalpha():
            
            if number in words:
                number = number * 10
                
                print('The number you entered is {}!'.format(number))
                
            else:
                print('Sorry, that number is not in the list!')
                
        else:
            print('Sorry, that number is not in the list!')
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        