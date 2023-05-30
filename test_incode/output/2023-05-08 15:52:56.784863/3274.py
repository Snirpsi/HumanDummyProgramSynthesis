#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that iterates over user input.
    while True:
        command = input('Enter a command: ')
        if command == 'exit':
            break
        else:
            print(command)

