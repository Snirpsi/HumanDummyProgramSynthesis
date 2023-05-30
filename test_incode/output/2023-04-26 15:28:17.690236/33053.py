#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or returns words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'user':
            
            print('User input:')
            
            print('\n'.join(map(str, input('\n> ').split())))
            
        elif sys.argv[1] == 'words':
            
            print('Words:')
            
            print('\n'.join(map(str, input('\n> ').split())))
            
        else:
            
            print('Unknown command.')
            
    else:
        
        print('Usage: python server.py [user|words]')
        
