#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers and prints numbers. """    
    
    numbers = input("Enter numbers: ")
    
    for number in numbers.split():
        print(number)
    
    print("Done!")
    
