#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or removes numbers. """    
    while True:
        command = input('> ')
        if command == 'quit':
            break
        elif command == '':
            continue
        elif command == 'help':
            print('''
            Commands:
                quit: Quit the program.
                help: Show this help message.
                ''')
        elif command == 'convert':
            number = input('Enter a number: ')
            number = int(number)
            print(str(number) + ' is converted.')
        elif command == 'remove':
            number = input('Enter a number: ')
            number = int(number)
            print(str(number) + ' is removed.')
        else:
            print('Unknown command.')
