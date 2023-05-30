#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that prints user input.
    while True:
        command = input('Enter a command: ')
        if command == 'exit':
            break
        elif command == 'help':
            print('Enter a command: help')
        else:
            print('Invalid command')

