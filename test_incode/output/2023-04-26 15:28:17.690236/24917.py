#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # User input - open and read a file
        
        with open(sys.argv[1]) as f:
            
            # Iterate over numbers in the file
            
            for n in f:
                
                print(n)
                
    else:
        
        # User input - open and read a string
        
        s = input('Enter a number: ')
        
        print(s)
        
    
