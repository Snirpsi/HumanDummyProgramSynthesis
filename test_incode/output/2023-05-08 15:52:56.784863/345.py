#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that removes a list of numbers.
    #The program will ask the user to enter a list of
    #numbers and then it will remove all the
    #numbers in the list.
    numbers = input("Enter a list of numbers: ")
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    print(numbers)
    numbers = numbers.remove(*numbers)
    print(numbers)

