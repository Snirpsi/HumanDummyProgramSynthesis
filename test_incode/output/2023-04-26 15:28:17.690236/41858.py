#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers or opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number > 0:
            
            print(number * 2)
            
        else:
            
            print(0)
            
    else:
        
        print(0)
        
