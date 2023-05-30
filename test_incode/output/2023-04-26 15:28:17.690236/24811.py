#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # User input was given
        if sys.argv[1] == 'user':
            
            # Get user input
            user = input("Enter a number: ")
            
            # Print number
            print(user)
            
        else:
            
            # Print number
            print(int(sys.argv[1]))
            
    else:
        
        # Print number
        print(int(sys.argv[1]))
        
    
