#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        command = input('> ')
        if command == 'quit':
            break
        elif command == 'help':
            print('''
            Commands:
                quit: quit this program
                help: print this help message
            ''')
        elif command == 'quit':
            print('Goodbye!')
            break
        else:
            print('Unknown command: {}'.format(command))
            
