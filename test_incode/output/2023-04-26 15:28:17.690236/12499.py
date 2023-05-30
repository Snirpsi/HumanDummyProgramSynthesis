#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers and iterates over a port. """    
    port = int(sys.argv[1])
    
    while(True):
        
        number = int(input("Enter a number: "))
        
        if(number > 0):
            
            print(number, "is", 