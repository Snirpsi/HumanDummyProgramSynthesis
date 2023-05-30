#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words or converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Parse the command line arguments
        
        mode = sys.argv[1]
        
        if mode == 'convert':
            
            # Convert user input into words
            
            words = convert_input(sys.argv[2])
            
            print(words)
            
        elif mode == 'words':
            
            # Return user input as a list of words
            
            words = convert_input(sys.argv[2])
            
            print(words)
            
        else:
            
            # Invalid mode
            
            print('Invalid mode')
            
    else:
        
        # No arguments given
        
        print('No arguments given')
        
    
