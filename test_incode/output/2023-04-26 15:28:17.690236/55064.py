#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and multiplyes numbers. """    
    
    while True:
        number = int(input('Enter a number: '))
        
        if number == -1:
            break
        
        print('The product is', number * number)
        
    print('Thank you for using the multiplication program!')
    
