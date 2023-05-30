#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that requests numbers.
    while True:
        print(numbers)
        numbers = input("Enter numbers: ")
        if numbers == 'done':
            break
        else:
            numbers = [int(n) for n in numbers.split(',')]
    print(numbers)

