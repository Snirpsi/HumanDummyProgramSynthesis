#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input. """    
    while True:
        command = input('Enter a command: ')
        if command == 'quit':
            break
        else:
            print(command)
