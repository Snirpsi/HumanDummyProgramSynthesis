#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input or enumerates a list of numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        number = input("Enter a number: ")
        
        if number == "exit":
            break
        
        if number in numbers:
            print("Number found:", number)
        else:
            print("Number not found:", number)
    
    print("Done!")
    
