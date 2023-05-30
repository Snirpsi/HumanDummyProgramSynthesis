#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or adds numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = 'add'
    
    if command == 'add':
        add()
    elif command == 'numbers':
        numbers()
    else:
        print('Unknown command')
        
