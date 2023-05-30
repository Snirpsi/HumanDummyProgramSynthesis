#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that requests numbers.
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        else:
            numbers.append(int(number))
    print(numbers)

