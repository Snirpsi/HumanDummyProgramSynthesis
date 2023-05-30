#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        command = input('> ')
        if command == 'exit':
            break
        elif command == 'quit':
            break
        elif command == 'help':
            print('''
            Commands:
            exit: Exit the program.
            quit: Quit the program.
            help: Print this help message.
            ''')
        else:
            print('Invalid command.')

<|/ file source=github filename=main.py |>