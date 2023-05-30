#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or opens fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = 'add'
    
    if command == 'add':
        add(sys.argv[2:])
    elif command == 'open':
        open(sys.argv[2:])
    else:
        print('Invalid command')
        
