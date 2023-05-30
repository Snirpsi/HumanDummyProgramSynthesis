#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or iterates over user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number % 2 == 0:
                print('{} is an even number.'.format(number))
            else:
                print('{} is an odd number.'.format(number))
        except ValueError:
            print('Invalid input. Try again.')
        except KeyboardInterrupt:
            print('Program terminated.')
            break
        else:
            break
