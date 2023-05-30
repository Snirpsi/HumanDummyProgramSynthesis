#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        command = input('> ')
        if command == 'exit':
            break
        else:
            command = command.split()
            command = command[0]
            command = command[1:]
            if command == 'help':
                print('''
                Commands:
                    exit: Exit the program.
                    help: Print this help message.
                    quit: Quit the program.
                    
                ''')
            elif command == 'quit':
                exit()
            elif command == 'help':
                print('''
                Commands:
                    quit: Quit the program.
                    help: Print this help message.
                    
                ''')
            else:
                print('Unrecognized command: ' + command)
