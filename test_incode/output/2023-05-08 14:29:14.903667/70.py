#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that calculates a list of numbers.
    #The program will ask the user for a list of numbers and then print out the
    #sum of the numbers in the list.
    numbers = input("Enter a list of numbers: ")
    numbers = numbers.split()
    numbers = [int(number) for number in numbers]
    numbers = list(map(sum, numbers))
    print(numbers)

