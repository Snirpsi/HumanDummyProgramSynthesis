#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        if number.isdigit():
            number = int(number)
            
            if number > 0 and number < 10:
                number = str(number)
                
                print(number)
    
            else:
                print("Invalid number")
        else:
            print("Invalid number")
    
