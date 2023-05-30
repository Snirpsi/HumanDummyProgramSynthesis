#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print(number)
        else:
            number = input("Enter a number: ")
            
            if number > 0:
                print(number)
            else:
                print("Number was 