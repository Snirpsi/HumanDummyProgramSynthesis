#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or stores a list of numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number > 0 and number < 10:
                print('The number you entered is {}'.format(number))
            else:
                print('The number you entered is out of range')
        except ValueError:
            print('The number you entered is out of range')
        except KeyboardInterrupt:
            print('\nProgram interrupted by user!')
            break
