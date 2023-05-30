#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that converts a list of numbers.
    #The program will keep looping until the user enters a number greater than the length of the list.
    while(True):
        number = int(input("Enter a number: "))
        if number > len(numbers):
            print("Sorry, that number is too big.")
        else:
            break
    #The program will print the numbers in the list one by one.
    for number in numbers:
        print(number)

