#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers. """    
    while True:
        number = int(input('Enter a number: '))
        print('The number you entered is', number)
        
        if number == -1:
            print('Thank you for using the program!')
            break
        
        if number > 10:
            print('Sorry, number greater than 10')
            break
        
        if number < 0:
            print('Sorry, number less than 0')
            break
        
        