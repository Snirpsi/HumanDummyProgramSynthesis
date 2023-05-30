#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or calculates numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number > 0:
                print('The number you entered is greater than zero')
            else:
                print('The number you entered is less than zero')
        except ValueError:
            print('Invalid input')
        except KeyboardInterrupt:
            print('\nProgram terminated')
            break
        else:
            break
