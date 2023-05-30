#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers and opens user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number > 0 and number <= 10:
                print('The number you entered is ' + str(number))
            else:
                print('Invalid input')
        except ValueError:
            print('Invalid input')
        finally:
            print('Press enter to continue')
            
