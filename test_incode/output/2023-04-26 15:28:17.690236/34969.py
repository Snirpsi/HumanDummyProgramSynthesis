#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers or iterates over a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        number = input('Enter a number: ')
        
        if number.isdigit():
            number = int(number)
            
            if number < 10:
                number = str(number)
                
                print(number)
                
            else:
                number = str(number)
                
                number = number[::-1]
                
                print(number)
                
        else:
            print('Please enter a number')
            
