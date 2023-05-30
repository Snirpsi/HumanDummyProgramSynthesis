#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits or opens a list of numbers. """    
    
    fruit = input("Enter a fruit or a list of numbers: ")
    
    if fruit == "fruit":
        fruit()
    elif fruit == "list":
        fruit()
    else:
        print("Invalid input")
        
