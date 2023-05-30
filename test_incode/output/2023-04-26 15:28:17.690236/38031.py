#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input. """    
    while True:
        command = input('Enter a command: ')
        command = command.strip()
        if command == 'exit':
            break
        elif command == 'help':
            print('''
            Commands:
            exit: Exit the program.
            help: Print this help message.
            ''')
        else:
            print('Unknown command: ' + command)
            
