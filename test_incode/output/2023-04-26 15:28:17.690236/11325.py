#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == '-':
            
            numbers = sys.stdin.readlines()
            
        else:
            
            numbers = open(sys.argv[1]).readlines()
            
    else:
        
        numbers = sys.stdin.readlines()
        
    for number in numbers:
        
        print(number)
        
