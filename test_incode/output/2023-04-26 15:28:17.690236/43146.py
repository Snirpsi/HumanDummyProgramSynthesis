#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or opens numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Try again.')
            continue
    
    if number > 10:
        print('You entered a number greater than 10. Try again.')
    else:
        print('You entered a number less than 10. Try again.')
        
