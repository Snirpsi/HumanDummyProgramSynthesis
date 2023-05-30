#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        command = input('Enter command: ')
        if command == 'exit':
            break
        else:
            print('You entered:', command)
            print('