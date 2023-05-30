#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or iterates over user input. """    
    
    while(True):
        try:
            number = int(input('Enter a number: '))
            if number > 0 and number < 10:
                print('The number you entered is ' + str(number))
            else:
                print('Please enter a number between 1 and 10.')
        except ValueError:
            print('Please enter a number.')
            
