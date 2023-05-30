#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that calculates a list of numbers.
    #The loop will run until the user enters 0.
    while True:
        numbers = numbers + [input("Enter a number: ") for _ in range(int(input("How many numbers would you like to add?: ")))]
        if int(input("Enter a number: ")) == 0:
            break
    print(numbers)

