#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that calculates a list of numbers.
    #The program will keep on running until the user enters q to quit.
    while True:
        numbers = numbers + [input("Enter a number: ") for _ in range(int(input("How many numbers?: ")))]
        if input("Do you want to continue? [y/n] ").lower() == "y":
            break
    print(numbers)

