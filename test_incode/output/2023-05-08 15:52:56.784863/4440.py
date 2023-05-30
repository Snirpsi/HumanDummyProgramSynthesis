#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that iterates over a list of numbers.
    #It prints the numbers in reverse order.
    #The function can be called from another program or from main.
    for number in numbers:
        print(number)
        number = number[::-1]
    print(numbers)

