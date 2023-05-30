#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or opens words. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            print('No port number given.')
        else:
            print('Opening words on port ' + str(port))
            open_word(port)
            print('Done.')
