#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads numbers from it
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Try again.")
        else:
            print(number)
            break
    #A endless loop that opens numbers.txt and reads numbers from it
    
    
    

