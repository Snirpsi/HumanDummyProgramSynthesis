#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        choice = sys.argv[1]
        
        if choice == '1':
            
            print('You chose option 1')
            
        elif choice == '2':
            
            print('You chose option 2')
            
        elif choice == '3':
            
            print('You chose option 3')
            
        elif choice == '4':
            
            print('You chose option 4')
            
        else:
            
            print('Invalid choice')
            
    else:
        
        print('No input given')
        
