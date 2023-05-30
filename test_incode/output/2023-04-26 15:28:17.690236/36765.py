#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Parse command line arguments
        
        words = []
        
        for arg in sys.argv[1:]:
            
            # Parse arguments
            
            word = arg.split('=')
            
            if len(word) == 1:
                
                # Ignore empty arguments
                
                continue
            
            words.append(word[0])
            
    else:
        
        # No arguments given
        
        words = ['word']
        
    
    # Print the results
    
    print('\n'.join('