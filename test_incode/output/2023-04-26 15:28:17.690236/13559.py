#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or converts user input. """    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number > 0 and number <= 10:
            
            number = str(number)
            
            print(number)
            
        else:
            
            print("Wrong input")
            
    else:
        
        print("Wrong input")
        
