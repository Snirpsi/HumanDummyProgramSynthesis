#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number == 999:
            print("Goodbye!")
            break
        else:
            print(number)
        
    
<|/ file filename=