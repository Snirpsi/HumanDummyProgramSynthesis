#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        command = sys.argv[1]
        
        if command == 'convert':
            
            print('Converting numbers...')
            
            number = int(input('Enter a number: '))
            
            print('Converted number:', number)
            
        elif command == 'print':
            
            print('Printing numbers...')
            
            number = int(input('Enter a number: '))
            
            print('Printing number:', number)
            
        else:
            
            print('Invalid command.')
            
    else:
        
        print('Usage: python3 webserver.py convert')
        
