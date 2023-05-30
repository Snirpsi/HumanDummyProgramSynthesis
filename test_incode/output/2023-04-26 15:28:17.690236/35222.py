#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        command = input('> ')
        if command == 'quit':
            break
        elif command == 'help':
            print('''
            Commands:
            quit: Quit the program.
            help: Print the help message.
            ''')
        else:
            command = command.split()
            command = command[0]
            if command == 'help':
                print('''
                Commands:
                quit: Quit the program.
                help: Print the help message.
                ''')
            else:
                command = command[1:]
                command = command[0]
                if command == 'quit':
                    break
                else:
                    command = command[1:]
                    command = command[0]
                    if command == 'help':
                        print('''
                        Commands:
                        quit: Quit the program.
                        help: Print the help message.
                        ''')
                    else:
                        command = command[1:]
                        command = command[0]
                        if command == 'help':
                            print('''
                            Commands:
                            quit: Quit the program.
                            help: Print the help message.
                            ''')
                        else:
                            command = command[1:]
                            command = command[0]
                            if command == 'quit':
                                break
                            else:
                                command = command[1:]
                                command = command[0]
                                if command == 'help':
                                    print('''
                                    Commands:
                                    quit: Quit the program.
                                    help: Print the help message.
                                    ''')
                                else:
                                    command = command[1:]
                                    command = command[0]
                                    if command == 'quit':
                                        break
                                    else:
                                        command = command[1:]
                                        command = command[0]
                                        if command == 'help':
                                            print('''
                                            Commands:
                                            quit: Quit the program.
                                            help: Print the help message.
                                            ''')
                                        else:
                                            command = command[1:]
                                            command = command[0]
                                            if command == 'quit':
                                                break
                                            else:
                                                command = command[1:]
                                                command = command[0]
                                                if command == 'help':
                                                    print('''
                                                    Commands:
                                                    quit: Quit the program.
                                                    help: Print the help message.
                                                    ''')
                                                else:
                                                    command = command[1:]
                                                    command = command[0]
                                                    if command == 'quit':
                                                        break
                                                    else:
                                                        command = command[1:]
                                                        command = command[0]
                                                        if command == 'help':
                                                            print('''
                                                            Commands:
                                                            quit: Quit the program.
                                                            help: Print the help message.
                                                            ''')
                                                        else:
                                                            command = command[1:]
                                                            command = command[0]
                                                            if command == 'quit':
                                                                break
                                                            else:
                                                                command = command[1:]
                                                                command = command[0]
                                                                if command == 'help