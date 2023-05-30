#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or prints a list of numbers. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            print('Exiting...')
            break
        else:
            print('Converting port {} to binary...'.format(port))
            binary = convert_port(port)
            print('Converted port {} to binary...'.format(port))
            print('Binary of port {} is {}'.format(port, binary))
            print('')
            print('List of binary digits:')
            for digit in binary:
                print('  {}'.format(digit))
            print('')
            print('Enter a number to exit')
            number = input('Enter a number to exit: ')
            if number == '':
                print('Exiting...')
                break
            else:
                print('Exiting...')
                break

<|/ file source=github ext=.py |>