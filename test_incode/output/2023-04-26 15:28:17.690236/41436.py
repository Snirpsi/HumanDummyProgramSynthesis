#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = 'help'
    
    if command == 'help':
        print('''
        Usage: python webserver.py [command]

        Available commands:
            help       - Display this help message
            quit       - Quit the server
            
        ''')
        
    elif command == 'quit':
        sys.exit(0)
    
    else:
        print('''
        Unknown command: '%s'

        ''' % command)
        
