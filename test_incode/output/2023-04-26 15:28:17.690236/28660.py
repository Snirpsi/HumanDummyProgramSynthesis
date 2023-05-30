#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or prints a port. """    
    while True:
        try:
            port = int(input('Enter a port: '))
            break
        except ValueError:
            print('Please enter a number.')
            continue
    print('Opening port {}'.format(port))
    