#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input. """    
    while True:
        multiplier = int(input("Enter a number: "))
        
        if multiplier == 0:
            break
        else:
            print(multiplier * multiplier)
            
