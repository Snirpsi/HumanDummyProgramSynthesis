#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        command = input("Enter a command: ").lower()
        if command == 'exit':
            break
        elif command == 'help':
            print('''
            Commands:
            exit: Exit the program
            help: Print this help message
            ''')
        else:
            print('Unknown command: ' + command)
