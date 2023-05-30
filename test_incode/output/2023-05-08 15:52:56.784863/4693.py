#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    while True:
        print(numbers)
        numbers.append(input("Enter a number: "))
        #A endless loop that prints the list after each number has been entered.
        #This loop will continue until the user enters a number that is not a number in the list.
        #The program will then print a message saying "Invalid input".
        if numbers[-1].isdigit():
            break
        else:
            print("Invalid input")

