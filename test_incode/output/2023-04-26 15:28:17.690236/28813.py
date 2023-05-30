#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or calculates a list of numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number > 0 and number < 10:
                number = str(number)
                print('The number is', number)
            else:
                print('Please enter a number between 0 and 10')
        except ValueError:
            print('Please enter a number')
        except KeyboardInterrupt:
            print('\nBye!')
            break
