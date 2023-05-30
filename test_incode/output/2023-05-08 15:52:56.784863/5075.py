#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that removes user input.
    while True:
        command = input('Enter a command: ')
        if command == 'exit':
            break
        else:
            print('You entered: ' + command)
            command = input('Enter a command: ')

