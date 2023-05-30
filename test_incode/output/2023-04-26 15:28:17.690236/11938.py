#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input or calculates numbers. """    
    
    number = input("Enter a number: ")
    
    if number == "quit":
        print("Goodbye")
        quit()
    else:
        number = int(number)
        
        print("The number is", number)
        
        print("The square root of ", number, " is ", math.sqrt(number))
        
        print("The square root of ", number, " is ", math.pow(number, 2))
        
        print("The square root of ", number, " is ", math.pow(number, 