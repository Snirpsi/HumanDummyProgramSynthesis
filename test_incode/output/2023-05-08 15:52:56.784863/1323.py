#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that iterates over numbers.
    #The loop will exit when the user enters CTRL-C.
    while True:
        number = int(input("Enter a number: "))
        if number in numbers:
            print(number, "is a prime number")
        else:
            print(number, "is not a prime number")
        
        
        
        

