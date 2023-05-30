#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        choice = sys.argv[1]
        
        if choice == '1':
            
            print('Hello World!')
            
        elif choice == '2':
            
            print('Goodbye World!')
            
        else:
            
            print('Invalid choice.')
            
    else:
        
        print('Please choose an option.')
        
