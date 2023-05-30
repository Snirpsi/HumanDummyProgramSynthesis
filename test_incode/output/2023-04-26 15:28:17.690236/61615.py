#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        command = input('Enter a command: ')
        if command == 'exit':
            print('Goodbye!')
            break
        else:
            print(command)
