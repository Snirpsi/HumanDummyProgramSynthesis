#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        command = input('> ')
        if command == 'quit':
            break
        
        command = command.split()
        
        if command[0] == 'help':
            print('''
            Commands:
            
            help: Prints this help message.
            quit: Quits this program.
            ''')
        elif command[0] == 'exit':
            print('''
            Goodbye.
            ''')
        else:
            print('''
            Unknown command: '%s'
            ''' % command[0])
            
