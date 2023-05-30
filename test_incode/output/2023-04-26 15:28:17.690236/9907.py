#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'user':
            user = input('Enter your name: ')
            print('Hello ' + user + '!')
        elif command == 'convert':
            user = input('Enter your name: ')
            number = int(input('Enter a number: '))
            
            print('The number you entered is', number)
        else:
            print('Invalid command')
    else:
        print('Usage: python webserver.py [user|convert]')
        
