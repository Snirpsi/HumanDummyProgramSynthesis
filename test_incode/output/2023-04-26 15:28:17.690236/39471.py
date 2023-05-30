#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        number = input("Enter a number: ")
        
        if number == "":
            break
        
        if number in numbers:
            print("{} is a prime number".format(number))
        else:
            print("{} is not a prime number".format(number))
            
        print("-" * 50)
        
    print("Thank you for using 