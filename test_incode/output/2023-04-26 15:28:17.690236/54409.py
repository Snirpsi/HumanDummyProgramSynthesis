#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or returns user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Read command line arguments.
        
        words = sys.argv[1:]
        
    else:
        
        # Read user input.
        
        words = input("Enter a word: ")
        
    
    # Print the results.
    
    print("Words: ", words)
    
    
    # 