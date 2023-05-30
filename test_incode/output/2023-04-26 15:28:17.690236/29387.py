#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input or iterates over a list of numbers. """    
    
    number = input("Enter a number: ")
    
    if number == 'quit':
        print('Goodbye!')
        exit()
    
    try:
        number = int(number)
    except ValueError:
        print('That is not a number')
        
    if number < 0:
        print('Negative numbers are not allowed')
        
    if number > 1000:
        print('