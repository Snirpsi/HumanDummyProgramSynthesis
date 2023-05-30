#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        choice = sys.argv[1]
        
        if choice == '1':
            
            print('The user chose to enumerate all user input.')
            
        else:
            
            print('The user chose to enumerate user input with value "{}".'.format(choice))
            
    else:
        
        print('The user chose to enumerate user input with value "{}".'.format(1))
        
