#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or removes a list of words. """    
    
    while True:
        number = input('Enter a number: ')
        if number == 'quit':
            break
        
        if number.isdigit():
            print(int(number))
        else:
            print(number)
            
    print('Goodbye!')
    
