#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        command = sys.argv[1]
        
        if command == 'user':
            
            user_text = input('Enter a message:')
            
            print('Your message is: ' + user_text)
            
        elif command == 'iterate':
            
            user_text = input('Enter a message:')
            
            print('Your message is: ' + user_text)
            
        else:
            
            print('Invalid command')
            
    else:
        
        print('Usage: python3 webserver.py [user|iterate]')
        
