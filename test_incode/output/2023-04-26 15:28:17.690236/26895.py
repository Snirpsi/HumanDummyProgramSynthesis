#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input or prints user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'add':
            print('Adding user input')
            
        elif command == 'print':
            print('Printing user input')
            
        else:
            print('Unknown command')
            
    else:
        print('No command given')
        
