#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and prints fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape', 'mango']
    while True:
        port = input('Enter a port number: ')
        if port == '':
            print('No port number entered')
        else:
            print('Adding port number ' + port)
            