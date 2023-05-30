#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input and enumerates numbers. """    
    
    while True:
        number = input("Enter a number: ")
        
        if number == "quit":
            break
        
        number = int(number)
        
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
        
        print("Number:", number)
        
    print("Goodbye!")
    
