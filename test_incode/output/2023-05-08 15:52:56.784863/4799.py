#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    #The loop will run until the user enters 0.
    #The loop will then print out the numbers in the list.
    #The loop will then exit the program.
    while True:
        numbers_string = input("Enter a number: ")
        try:
            number = int(numbers_string)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            print(numbers)
            break

