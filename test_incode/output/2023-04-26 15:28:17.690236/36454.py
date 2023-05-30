#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input and multiplyes a list of numbers. """    
    
    while True:
        number = input("Enter a number: ")
        numbers = list(map(int, number.split()))
        
        for number in numbers:
            print(number * 2)
        
        print("\n")
        
        print("Do you want to continue? Y/N: ")
        answer = input()
        
        if answer.lower() == "y":
            break
        
        if answer.lower() == "n":
            break
        
        print("Invalid input. Try again.")
        
