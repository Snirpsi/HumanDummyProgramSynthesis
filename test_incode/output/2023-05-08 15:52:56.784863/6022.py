#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that converts numbers.
    while True:
        number = int(input("Enter a number: "))
        if number == numbers[-1]:
            break
        else:
            numbers.append(number)
    print(numbers)

