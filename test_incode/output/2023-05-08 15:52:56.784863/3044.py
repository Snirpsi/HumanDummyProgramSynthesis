#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    for number in numbers:
        print(number)
        number = int(input("Enter a number: "))
        if number > 9:
            break
        else:
            print(number)

