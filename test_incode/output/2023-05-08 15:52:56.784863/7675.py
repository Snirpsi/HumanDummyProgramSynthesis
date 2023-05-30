#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that removes numbers.
    #The loop will continue until a number is entered.
    while True:
        number = input("Enter a number: ")
        if number in numbers:
            numbers.remove(number)
        else:
            break
    print(numbers)

